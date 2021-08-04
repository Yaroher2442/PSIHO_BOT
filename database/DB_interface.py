import hashlib
import os
import binascii
import uuid
from database import models
from peewee import JOIN


class BaseDb:
    def __init__(self):
        self.database = models.pg_db
        self.table = None

    def set_row(self, **kwargs):
        try:
            new_row = self.table.create(**kwargs)
            return new_row
        except:
            return False

    def delete_row(self, id):
        try:
            to_delete = self.table.get(self.table.id == id)
            return to_delete.delete_instance()
        except:
            return False

    def update(self, id, **kwargs):
        try:
            up_dict = {}
            for k, v in kwargs.items():
                up_dict.update({getattr(self.table, k): v})
            query = self.table.update(up_dict).where(self.table.id == id)
            query.execute()
        except Exception as e:
            print(e)
            return False

    def get_by_element(self, col_name, value):
        try:
            return self.table.select().where(getattr(self.table, col_name) == value)
        except Exception as e:
            print(e)
            return False

    def get_by_id(self, id):
        try:
            return self.table.get(id=id)
        except Exception as e:
            print(e)
            return False

    def get_all(self, *args, order=None):
        try:
            if order:
                return self.table.select(*args).order_by(order)
            else:
                return self.table.select(*args)
        except Exception as e:
            print(e)
            return False

    def get_all_join(self, table_name, order, *args):
        try:
            return self.table.select(*args).join(getattr(models, table_name), JOIN.LEFT_OUTER).order_by(order)
        except Exception as e:
            print(e)
            return False


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

    def registry_user(self, name, email, passwrd):
        try:
            try:
                models.AdminUser.get(name=name)
                return False
            except:
                new_user = models.AdminUser.create(name=name, password=self.hash_password(passwrd), email=email,
                                                   token="")
                print(new_user)
                return True
        except Exception as e:
            return False

    def login_user(self, email, passwrd):
        try:
            user = models.AdminUser.get(email=email)
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
            user = models.AdminUser.get(token=req_token)
            print(user)
            return True
        except:
            print("User not found by token")
            return False


class StatusesApi(BaseDb):
    def __init__(self):
        BaseDb.__init__(self)
        self.table = models.Statuses


class MenuApi(BaseDb):
    def __init__(self):
        BaseDb.__init__(self)
        self.table = models.Menu


class MenuButtonApi(BaseDb):
    def __init__(self):
        BaseDb.__init__(self)
        self.table = models.MenuButton


class TextAnswersApi(BaseDb):
    def __init__(self):
        BaseDb.__init__(self)
        self.table = models.TextAnswers


class CommandsApi(BaseDb):
    def __init__(self):
        BaseDb.__init__(self)
        self.table = models.Commands


class DBInterface:
    def __init__(self):
        self.auth = Auth()
        self.Menu = MenuApi()
        self.Statuses = StatusesApi()
        self.MenuButton = MenuButtonApi()
        self.TextAnswers = TextAnswersApi()
        self.Commands = CommandsApi()
