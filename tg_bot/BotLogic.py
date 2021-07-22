from fuzzywuzzy import fuzz
from telebot import types
from database.models import *


class Answer:
    def __init__(self, message):
        self.returns_answr = ""
        self.message = message
        self.reply_markup = None
        self.user_id = message.from_user.id
        self.user_obj = None  # +
        self.block = None  # +
        self.menu = None  # +
        self.buttons = None  # +
        self.text_answr_obj = None
        self.button_pressed = None
        self.change_status_to = None
        self.self_initial()
        self.on_message()

    def on_message(self):
        print(self.__dict__)
        if self.validate_reg():
            self.get_text_answr()
        else:
            self.returns_answr = "Techical error reg_user"

    def validate_reg(self):
        if not self.user_obj:
            if self.reg_user():
                return True
            else:
                return False
        else:
            return True

    def get_text_answr(self):
        if self.button_pressed:
            self.returns_answr = self.button_pressed.text
        elif self.text_answr_obj:
            self.returns_answr = self.text_answr_obj.answer
        else:
            self.returns_answr = "Techical error get_text_answr"

    def self_initial(self):
        self.get_user()
        self.get_block()
        self.get_menu()
        self.get_text_answr_obj()
        self.check_is_button_press()
        self.check_change_status()

    def reg_user(self):
        try:
            self.user_obj = TgClient.create(tg_id=self.message.from_user.id, status=1)
            return True
        except Exception as e:
            print(e)
            return False

    def get_user(self):
        try:
            self.user_obj = TgClient.get(tg_id=self.user_id)
        except Exception as e:
            print(e)
            return None

    def get_block(self):
        if self.user_obj:
            try:
                self.block = Block.get(status_id=self.user_obj.status)
            except Exception as e:
                print(e)

    def get_menu(self):
        try:
            self.menu = Menu.get(id=self.block.menu_id)
        except Exception as e:
            print(e)
        if self.menu:
            try:
                self.buttons = MenuButton.select().where(MenuButton.menu_id == self.menu.id)
            except Exception as e:
                print(e)
        else:
            return None

    def get_text_answr_obj(self):
        try:
            self.text_answr_obj = TextAnswers.get(id=self.block.answer_id)
        except Exception as e:
            print(e)
            return None

    def check_is_button_press(self):
        if self.buttons:
            for btn in self.buttons:
                if btn.text == self.message.text:
                    self.button_pressed = btn
                    break
                else:
                    self.button_pressed = None

    def check_change_status(self):
        if self.button_pressed:
            self.change_status_to = self.button_pressed.to_status
        elif self.text_answr_obj:
            self.change_status_to = self.text_answr_obj.to_status

    def change_status(self):
        if self.change_status_to:
            self.user_obj.status = self.change_status_to
            self.user_obj.save()


class BotUseLogic:
    def __init__(self):
        self.db = pg_db

    def answr_text(self, message):
        pass

    def get_menu(self, message):
        pass

    def start_command(self, message):
        try:
            client = TgClient.get(id=message.from_user.id)
        except:
            return False


if __name__ == '__main__':
    pass
