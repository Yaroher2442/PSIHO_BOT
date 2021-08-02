from fuzzywuzzy import fuzz
from telebot import types
from database.models import *
from config.loger import AppLogger
import json
import builtins


class Answer:
    def __init__(self, message, logger: AppLogger):
        self.logger = logger
        self.message = message

        self.statistic = AnswersStatistic(tg_user_id=self.message.from_user.id, question=self.message.text,
                                          datetime=self.message.date)

        self.returns_answr = ""
        self.reply_markup = None

        self.user_id = message.from_user.id
        self.user_obj = None  # +
        self.user_status = None

        self.text_answr_obj = None

        self.current_menu = None  # +
        self.button_pressed = None

        self.new_status = None
        self.new_menu = None
        self.new_btns = None

        self.self_initial()
        self.on_message()
        self.logger.info(self.__dict__)

    def on_message(self):
        self.validate_user()
        if self.user_obj:
            if self.text_answr_obj:
                self.returns_answr = self.text_answr_obj.answer
                if self.new_status:
                    self.update_user_status()
                self.placeholders()
            else:
                self.returns_answr = "Извините, не могу определить ваш запрос. Пожалуйста, попробуйте ещё раз"
            self.statistic.answer = self.returns_answr
            self.statistic.save()
            self.generate_menu()
        else:
            self.returns_answr = "Techical error vlidate_user"

    def self_initial(self):
        self.validate_user()
        self.get_current_menu()
        self.check_msg_is_button()
        self.get_txt_answr_obj()
        self.new_status_state()

    def placeholders(self):
        pass

    def validate_user(self):
        try:
            self.user_obj = TgClient.get(tg_id=self.user_id)
            self.user_status = self.user_obj.status
        except Exception as e:
            try:
                self.user_obj = TgClient.create(tg_id=self.message.from_user.id, status=1,
                                                first_name=self.message.from_user.first_name,
                                                last_name=self.message.from_user.last_name,
                                                username=self.message.from_user.username)
                self.user_status = self.user_obj.status
            except Exception as e:
                self.logger.error(e)

    def update_user_status(self):
        try:
            self.user_obj.status = self.new_status
            self.user_obj.save()
        except Exception as e:
            self.logger.error(e)
            return False

    def get_current_menu(self):
        try:
            self.current_menu = Menu.get(Menu.status == self.user_status)
        except Exception as e:
            self.logger.error(e)

    def check_msg_is_button(self):
        try:
            btns = MenuButton.select().where(MenuButton.menu_id == self.current_menu.id)
            if self.message.text in [btn.text for btn in btns]:
                self.button_pressed = MenuButton.get(MenuButton.text == self.message.text)
        except Exception as e:
            self.logger.error(e)

    def get_txt_answr_obj(self):
        try:
            if self.button_pressed:
                self.text_answr_obj = TextAnswers.get(TextAnswers.question == self.button_pressed.text)
            else:
                try:
                    if '/' in self.message.text:
                        self.text_answr_obj = TextAnswers.get(TextAnswers.question == self.message.text)
                    else:
                        self.text_answr_obj = TextAnswers.get(TextAnswers.question == self.message.text,
                                                              TextAnswers.on_status == self.user_status)
                except:
                    for answer in TextAnswers.select().where(TextAnswers.on_status == self.user_status):
                        if answer.use_same_texts and fuzz.WRatio(answer.question, self.message.text) > 80:
                            self.text_answr_obj = answer
        except Exception as e:
            self.logger.error(e)
            return False

    def new_status_state(self):
        try:
            if self.text_answr_obj and self.text_answr_obj.to_status:
                self.new_status = self.text_answr_obj.to_status
                self.new_menu = Menu.get(status=self.new_status)
                self.new_btns = MenuButton.select().where(MenuButton.menu_id == self.new_menu.id)
        except Exception as e:
            self.logger.error(e)

    def generate_menu(self):
        if self.new_menu:
            splitter = lambda lst, sz: [lst[i:i + sz] for i in range(0, len(lst), sz)]
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            for btn in splitter(self.new_btns, 2):
                row = []
                for r in btn:
                    row.append(types.KeyboardButton(text=r.text))
                keyboard.row(*row)
            self.reply_markup = keyboard
