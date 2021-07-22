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
    descr = CharField()

    class Meta:
        database = pg_db


class TgClient(Model):
    tg_id = IntegerField()
    status = ForeignKeyField(Statuses)

    class Meta:
        database = pg_db


class Menu(Model):
    descr = CharField()
    status = ForeignKeyField(Statuses, on_delete="CASCADE", null=True)

    class Meta:
        database = pg_db


class TextAnswers(Model):
    question = CharField()
    answer = CharField()
    use_same_texts = BooleanField()
    to_status = ForeignKeyField(Statuses, on_delete="CASCADE", null=True)

    class Meta:
        database = pg_db


class MenuButton(Model):
    menu_id = ForeignKeyField(Menu, on_delete="CASCADE")
    text = CharField()

    class Meta:
        database = pg_db


class AdminUser(Model):
    name = CharField()
    password = CharField()
    token = CharField()

    class Meta:
        database = pg_db


if __name__ == '__main__':
    print(Menu.set_menu("qwrqwr"))
    print(Menu.select()[-1].descr)
