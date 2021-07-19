from database.models import *
from telebot import types
import fuzzywuzzy
from fuzzywuzzy import fuzz
from fuzzywuzzy import process


# print(Statuses)
# pg_db.create_tables([Statuses])
class BaseDB:
    def __init__(self):
        self.database = pg_db
        self.tables = [Statuses,
                       TG_Client,
                       Menu,
                       MenuButton,
                       ButtonAnswers,
                       TextAnswers]

    def create_db(self):
        with self.database:
            self.database.create_tables(self.tables)

    def get_status(self):
        pass

    def incriment_user_status(self, message):
        client = TG_Client.get(TG_Client.tg_id == message.from_user.id)
        client.status += 1
        client.save()

    def create_menu(self, message):
        client = TG_Client.get(TG_Client.tg_id == message.from_user.id)
        menu = Menu.get(Menu.status == client.status)
        menu_text = menu.descr
        buttons = MenuButton.select().where(ButtonAnswers.menu_button_obj == menu).get()
        return menu_text, buttons

    def get_button_answer(self, message):
        client = TG_Client.get(TG_Client.tg_id == message.from_user.id)
        menu = Menu.get(Menu.status == client.status)
        buttons = MenuButton.select().where(ButtonAnswers.menu_button_obj == menu).get()
        for button in buttons:
            if message.text == button.text:
                if button.next_menu:
                    self.incriment_user_status(message)
                    return self.create_menu(message)
                else:
                    btn_anwer = ButtonAnswers.get(ButtonAnswers.menu_button_obj == button)
                    return btn_anwer
        return False

    def get_same_texts(self, msg_text, bd_text):
        return fuzz.WRatio(msg_text, bd_text)

    def get_text_answer(self, message):
        menu_text, btn_answer = self.get_button_answer(message)
        if not btn_answer:
            text_answers = TextAnswers.select()
            for anwr in text_answers:
                if anwr.question == message.text:
                    return anwr.answer
                elif anwr.use_same_texts:
                    if self.get_same_texts(anwr.question, message.text) > 80:
                        return anwr.answer
                    else:
                        print('cant answer to this')
                else:
                    print('cant answer to this')
        else:
            return menu_text, btn_answer


if __name__ == '__main__':
    BaseDB().create_db()
