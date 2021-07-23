from database.models import *
import hashlib
import os
import binascii
import uuid


class BaseDb:
    def __init__(self):
        self.database = pg_db
        self.tables = [Statuses,
                       TgClient,
                       Menu,
                       MenuButton,
                       TextAnswers,
                       AdminUser]

    def create_db(self):
        with self.database:
            self.database.create_tables(self.tables)


class Auth(BaseDb):
    def __init__(self):
        BaseDb.__init__(self)

    def hash_password(self, password):
        salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
        pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'),
                                      salt, 100000)
        pwdhash = binascii.hexlify(pwdhash)
        return (salt + pwdhash).decode('ascii')

    def verify_password(self, stored_password, provided_password):
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
            try:
                AdminUser.get(name=name)
                return False
            except:
                new_user = AdminUser.create(name=name, password=self.hash_password(passwrd), token="")
                print(new_user)
                return True
        except Exception as e:
            return False

    def login_user(self, name, passwrd):
        try:
            user = AdminUser.get(name=name)
        except:
            print("User not found bby name")
            return False
        if self.verify_password(user.password, passwrd):
            user.token = str(uuid.uuid4())
            user.save()
            return user.token
        else:
            return False

    def verify_token(self, req_token):
        try:
            user = AdminUser.get(token=req_token)
            return True
        except:
            print("User not found by token")
            return False


class MenuApi(BaseDb):
    def __init__(self):
        BaseDb.__init__(self)

    def set_new(self, menu_description="", status=None):
        try:
            new_menu = Menu.create(descr=menu_description, status=status)
            return new_menu.id
        except:
            return False

    def update_text(self, menu_id, text):
        try:
            query = Menu.update({Menu.descr: text}).where(Menu.id == menu_id)
            query.execute()
            return True
        except:
            return False

    def get_by_id(self, menu_id):
        return Menu.get(id=menu_id)


class MenuButtonApi(BaseDb):
    def __init__(self):
        BaseDb.__init__(self)

    def set_new(self, text="", next_menu_id=0, btn_answer=""):
        try:
            new_menu_button = MenuButton.create(text=text, next_menu=next_menu_id,
                                                answer=btn_answer)
            return new_menu_button.id
        except:
            return False

    def update_text(self, menu_button_id: int, text: str):
        try:
            query = MenuButton.update({MenuButton.text: text}).where(MenuButton.id == menu_button_id)
            query.execute()
            return True
        except:
            return False

    def update_answer(self, menu_button_id: int, btn_answer: str):
        try:
            query = MenuButton.update({MenuButton.answer: btn_answer}).where(MenuButton.id == menu_button_id)
            query.execute()
            return True
        except:
            return False

    def update_next_menu(self, menu_button_id: int, next_menu_id: int):
        try:
            query = MenuButton.update({MenuButton.next_menu: next_menu_id}).where(MenuButton.id == menu_button_id)
            query.execute()
            return True
        except:
            return False

    def get_by_id(self, menu_button_id):
        return MenuButton.get(id=menu_button_id)

    def get_all_buttons(self, menu_id):
        return MenuButton.select().where(MenuButton.id == menu_id)


class TextAnswersApi(BaseDb):
    def __init__(self):
        BaseDb.__init__(self)

    def set_new(self, question="", answer="", use_same_texts=False, change_state_to=0):
        try:
            new_menu_text = MenuButton.create(question=question, answer=answer,
                                              use_same_texts=use_same_texts, change_state_to=change_state_to)
            return new_menu_text.id
        except:
            return False

    def update_question(self, text_anwer_id: int, question: str):
        try:
            query = TextAnswers.update({TextAnswers.question: question}).where(TextAnswers.id == text_anwer_id)
            query.execute()
            return True
        except:
            return False

    def update_answer(self, text_anwer_id: int, answer: str):
        try:
            query = TextAnswers.update({TextAnswers.answer: answer}).where(TextAnswers.id == text_anwer_id)
            query.execute()
            return True
        except:
            return False

    def update_use_same(self, text_anwer_id: int, use_same_texts: bool):
        try:
            query = TextAnswers.update({TextAnswers.use_same_texts: use_same_texts}).where(
                TextAnswers.id == text_anwer_id)
            query.execute()
            return True
        except:
            return False

    def update_to_status(self, text_anwer_id: int, to_status: int):
        try:
            query = TextAnswers.update({TextAnswers.change_state_to: to_status}).where(
                TextAnswers.id == text_anwer_id)
            query.execute()
            return True
        except:
            return False

    def get_to_status(self, text_ansers_id: int):
        try:
            return TextAnswers.get(id=text_ansers_id).to_status
        except:
            return False

    def get_by_id(self, text_ansers_id):
        return TextAnswers.get(id=text_ansers_id)

    def get_by_text(self, text):
        try:
            return TextAnswers.get(question=text)
        except:
            return False

    def get_all(self):
        return TextAnswers.select()


class TgClientAPI(BaseDb):
    def __init__(self):
        BaseDb.__init__(self)

    def set_new(self, tg_id: int, status=0):
        try:
            new_tg_client = TgClient.create(tg_id=tg_id, status=status)
            return new_tg_client.id
        except:
            return False

    def set_status(self, tg_id: int, status: int):
        try:
            query = TgClient.update({TgClient.status: status}).where(TgClient.tg_id == tg_id)
            query.execute()
            return True
        except:
            return False

    def get_user(self, tg_id):
        try:
            client = TgClient.get(tg_id=tg_id)
            return client
        except:
            return False

    def get_status(self, tg_id):
        return TgClient.get(tg_id=tg_id).status


class ApiDB(BaseDb):
    def __init__(self):
        BaseDb.__init__(self)
        self.auth = Auth()
        self.Menu = MenuApi()
        self.MenuButton = MenuButtonApi()
        self.TextAnswers = TextAnswersApi()
        self.TgClient = TgClientAPI()


if __name__ == '__main__':
    pass
    # ApiDB()
    BaseDb().create_db()

    # ApiDB().TextAnswers.set_new(question='/start',answer='Привет я психобот')
    # BaseDb().create_db()
