from fuzzywuzzy import fuzz
from telebot import types
from database.models import *
from config.loger import AppLogger
import telebot
import json
import builtins
from datetime import datetime
import re

class Answer:
    def __init__(self, message, logger: AppLogger):
        self.logger = logger

        self.message = message
        self.user_obj = None

        self.status = None
        self.action = None
        self.command = None
        self.button = None

        self.new_status = None
        self.returns_answr = None
        self.reply_markup = None

        self.mode = 'text'
        self.process()

    def process(self):
        self.validate_user()
        if self.action == "listen":
            self.text_finder()
        if self.is_command():
            self.change_status()
            self.set_action()
            self.mode = "command"
        if self.is_button():
            self.change_status()
            self.set_action()
            self.mode = "button"
        self.rerender()

    def validate_user(self):
        try:
            self.user_obj = TgClient.get(tg_id=self.message.from_user.id)
            self.status = Statuses.get(Statuses.id == self.user_obj.status)
            self.action = self.status.action
        except Exception as e:
            self.logger.debug("User not found, try to create")
            try:
                self.user_obj = TgClient.create(tg_id=self.message.from_user.id, status=1,
                                                first_name=self.message.from_user.first_name,
                                                last_name=self.message.from_user.last_name,
                                                username=self.message.from_user.username)
                self.status = Statuses.get(Statuses.id == self.user_obj.status)
                self.action = self.status.action
            except Exception as e:
                self.logger.error("Can't create user")

    def is_command(self):
        if "/" in self.message.text:
            try:
                self.command = Commands.get(Commands.text == self.message.text)
                self.new_status = self.command.to_status
                self.returns_answr = self.command.answer
                return True
            except Exception as e:
                self.logger.debug("Can't found command")
                return False
        else:
            return False

    def is_button(self):
        try:
            self.button = MenuButton.get(MenuButton.text == self.message.text,
                                         MenuButton.menu_id == Menu.get(Menu.status == self.user_obj.status).id)
            self.new_status = self.button.to_status
            self.action = self.button.set_action
            self.returns_answr = self.button.answer
            return True
        except Exception as e:
            self.logger.debug(" button False")
            return False

    def change_status(self):
        try:
            self.user_obj.status = self.new_status
            self.user_obj.save()
        except Exception as e:
            self.logger.error("Can't set new status")

    def set_action(self):
        status = Statuses.get(Statuses.id == self.new_status)
        status.action = self.action
        status.save()

    def text_finder(self):
        try:
            for answr in TextAnswers.select():
                if fuzz.WRatio(answr.question, self.message.text) > 80:
                    self.returns_answr = answr.answer
        except Exception as e:
            return None

    def rerender(self):
        try:
            btns = MenuButton.select().where(MenuButton.menu_id == Menu.get(Menu.status == self.new_status.id).id)
            splitter = lambda lst, sz: [lst[i:i + sz] for i in range(0, len(lst), sz)]
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            for btn in splitter(btns, 2):
                row = []
                for r in reversed(btn):
                    row.append(types.KeyboardButton(text=r.text))
                keyboard.row(*row)
            self.reply_markup = keyboard
        except Exception as e:
            self.logger.debug("Can't found new menu render")
            return False

    def str_processor(self) -> list:
        try:
            if self.returns_answr:
                return [i for i in self.returns_answr.split('#message') if i]
            else:
                return ["Извините, не смог понять вас", "Попробуйте ещё раз"]
        except:
            return ["Извините, не смог понять вас", "Попробуйте ещё раз"]


    def send_message(self, bot: telebot.telebot):
        for msg in self.str_processor():
            bot.send_message(self.message.from_user.id,
                             text=msg,
                             reply_markup=self.reply_markup,
                             parse_mode="html")
