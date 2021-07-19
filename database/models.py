from peewee import *
from config.conf import Configurator

conf = Configurator()

pg_db = PostgresqlDatabase(host=conf.db_conf.host,
                           port=conf.db_conf.port,
                           database=conf.db_conf.db_name,
                           user=conf.db_conf.user,
                           password=conf.db_conf.user_pass,
                           )


class Statuses(Model):
    status = IntegerField()

    class Meta:
        database = pg_db


class TG_Client(Model):
    tg_id = IntegerField()
    status = ForeignKeyField(Statuses)

    class Meta:
        database = pg_db


class Menu(Model):
    descr = CharField()
    status = ForeignKeyField(Statuses)

    class Meta:
        database = pg_db


class MenuButton(Model):
    menu_obj = ForeignKeyField(Menu)
    text = CharField()
    next_menu = ForeignKeyField(Menu)

    class Meta:
        database = pg_db


class ButtonAnswers(Model):
    menu_button_obj = ForeignKeyField(MenuButton)
    text = CharField()

    class Meta:
        database = pg_db


class TextAnswers(Model):
    question = CharField()
    answer = CharField()
    use_same_texts = BooleanField()

    class Meta:
        database = pg_db


class AdminUser(Model):
    name = CharField()
    password = CharField()
    token = CharField()

    class Meta:
        database = pg_db


if __name__ == '__main__':
    pg_db.create_tables([Statuses])
