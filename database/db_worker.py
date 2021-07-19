import uuid

from database.models import *
from fuzzywuzzy import fuzz
import hashlib
import os
import binascii
class BaseDb:
    def __init__(self):
        self.database = pg_db
        self.tables = [Statuses,
                       TG_Client,
                       Menu,
                       MenuButton,
                       ButtonAnswers,
                       TextAnswers,
                       AdminUser]

    def create_db(self):
        with self.database:
            self.database.create_tables(self.tables)


class BotDB(BaseDb):
    def __init__(self):
        BaseDb.__init__(self)

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


class AdminDB(BaseDb):
    def __init__(self):
        BaseDb.__init__(self)

    def hash_password(self,password):
        salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
        pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'),
                                      salt, 100000)
        pwdhash = binascii.hexlify(pwdhash)
        return (salt + pwdhash).decode('ascii')

    def verify_password(self,stored_password, provided_password):
        salt = stored_password[:64]
        stored_password = stored_password[64:]
        pwdhash = hashlib.pbkdf2_hmac('sha512',
                                      provided_password.encode('utf-8'),
                                      salt.encode('ascii'),
                                      100000)
        pwdhash = binascii.hexlify(pwdhash).decode('ascii')
        return pwdhash == stored_password

    def registry_user(self, name, passwrd):
        try:
            new_user = AdminUser.create(name=name, password=self.hash_password(passwrd), token="")
            print(new_user)
            return True
        except Exception as e:
            print(e)
            return False

    def login_user(self, name, passwrd):
        try:
            user=AdminUser.get(name=name)
        except:
            print("User not found ")
            return False
        if self.verify_password(user.password, passwrd):
            user.token=str(uuid.uuid4())
            return user.token
        else:
            return False
    def set_new_menu(self):
        pass


if __name__ == '__main__':
    BaseDb().create_db()
