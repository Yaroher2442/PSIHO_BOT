from fuzzywuzzy import fuzz
from telebot import types
from database.models import *


class Answer:
    def __init__(self, message):
        self.message = message

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
        print(self.__dict__)

    def on_message(self):
        self.validate_user()
        if self.user_obj:
            try:
                self.returns_answr = self.text_answr_obj.answer

            except Exception as e:
                self.returns_answr=""
                print("without text", e)
            self.generate_menu()
            # if self.button_pressed and self.new_status:
            #     pass
            # elif self.button_pressed and not self.new_status:
            #     pass
        else:
            self.returns_answr = "Techical error vlidate_user"

    def self_initial(self):
        self.validate_user()
        self.get_current_menu()
        self.check_msg_is_button()
        self.get_txt_answr_obj()
        self.new_status_state()

    def validate_user(self):
        try:
            self.user_obj = TgClient.get(tg_id=self.user_id)
            self.user_status = self.user_obj.status
        except Exception as e:
            print(e)
            try:
                self.user_obj = TgClient.create(tg_id=self.message.from_user.id, status=1)
                self.user_status = self.user_obj.status
            except Exception as e:
                print(e)

    def get_current_menu(self):
        try:
            self.current_menu = Menu.get(Menu.status == self.user_status)
        except Exception as e:
            print(e)

    def check_msg_is_button(self):
        try:
            btns = MenuButton.select().where(MenuButton.menu_id == self.current_menu.id)
            if self.message.text in [btn.text for btn in btns]:
                self.button_pressed = MenuButton.get(MenuButton.text == self.message.text)
        except Exception as e:
            print(e)

    def get_txt_answr_obj(self):
        try:
            if self.button_pressed:
                self.text_answr_obj = TextAnswers.get(TextAnswers.question == self.button_pressed.text)
            else:
                try:
                    self.text_answr_obj = TextAnswers.get(TextAnswers.question == self.message.text)
                except:
                    for answer in TextAnswers.select():
                        if answer.use_same_texts and fuzz.WRatio(answer.question, self.message.text) > 80:
                            self.text_answr_obj = answer
        except Exception as e:
            print(e)
            return False

    def new_status_state(self):
        try:
            if self.text_answr_obj and self.text_answr_obj.to_status:
                self.new_status = self.text_answr_obj.to_status
                self.new_menu = Menu.get(status=self.new_status)
                self.new_btns = MenuButton.select().where(MenuButton.menu_id == self.new_menu.id)
        except Exception as e:
            print(e)

    def generate_menu(self):
        if self.new_menu:
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            for btn in self.new_btns:
                keyboard.add(types.KeyboardButton(text=btn.text))
            self.reply_markup = keyboard


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
