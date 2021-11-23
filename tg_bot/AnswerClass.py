from typing import List, Union

from fuzzywuzzy import fuzz
from loguru import logger
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup

from database.models import *
from config_.loger import AppLogger
import json
import builtins
from datetime import datetime
from telegram.ext import Updater, CallbackContext
from telegram.message import Message
import re


class Answer:
    def __init__(self, message: Message, logger: AppLogger):
        self.logger = logger
        self.message: Message = message

        self.statistic = AnswersStatistic(tg_user_id=self.message.chat_id, datetime=datetime.now(),
                                          question=self.message.text)
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
        with pg_db.atomic() as transaction:
            try:
                self.user_obj = TgClient.get(tg_id=self.message.from_user.id)
                self.status = Statuses.get(Statuses.id == self.user_obj.status)
                self.action = self.status.action
            except Exception as e:
                self.logger.warning(f"User not found, try to create {e}")
                try:
                    self.user_obj = TgClient.create(tg_id=self.message.chat.id,
                                                    status=Statuses.select().where(Statuses.action == None).order_by(Statuses.id).get(),
                                                    first_name=self.message.chat.first_name,
                                                    last_name=self.message.chat.last_name,
                                                    username=self.message.chat.username)
                    self.status = Statuses.get(Statuses.id == self.user_obj.status)
                    self.action = self.status.action
                except Exception as e:
                    transaction.rollback()
                    self.logger.error(f"Can't create user : {e}")

    def is_command(self):
        if "/" in self.message.text:
            try:
                self.command = Commands.get(Commands.text == self.message.text)
                self.new_status = self.command.to_status
                self.returns_answr = self.command.answer
                return True
            except Exception as e:
                self.logger.debug(f"Can't found command {e}")
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
            self.logger.debug(f"Button False {e}")
            return False

    def change_status(self):
        try:
            self.user_obj.status = self.new_status
            self.user_obj.save()
        except Exception as e:
            self.logger.error(f"Can't set new status {e}")

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

    def build_menu(self,
                   buttons: List[KeyboardButton],
                   n_cols: int,
                   ) -> List[List[KeyboardButton]]:
        return [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]

    def rerender(self):
        try:
            logger.debug(vars(self))
            btns = MenuButton.select().where(MenuButton.menu_id == Menu.get(Menu.status == self.new_status.id).id)
            # reply_markup = InlineKeyboardMarkup(self.build_menu(button_list, n_cols=2))
            button_list = []
            for btn in btns:
                button_list.append(KeyboardButton(btn.text))
            self.reply_markup = ReplyKeyboardMarkup(self.build_menu(button_list, n_cols=2))
        except Exception as e:
            self.logger.debug(f"Can't found new menu render {e}")
            return False

    def str_processor(self) -> list:
        try:
            if self.returns_answr:
                return [i for i in self.returns_answr.split('#message') if i]
            else:
                return ["Извините, не смог понять вас", "Попробуйте ещё раз"]
        except:
            return ["Извините, не смог понять вас", "Попробуйте ещё раз"]

    def send_message(self, context: CallbackContext):
        for msg in self.str_processor():
            context.bot.send_message(self.message.from_user.id,
                                     text=msg,
                                     reply_markup=self.reply_markup,
                                     parse_mode="html")
        if self.command or self.button:
            pass
        else:
            self.statistic.answer = self.returns_answr
            self.statistic.save()
