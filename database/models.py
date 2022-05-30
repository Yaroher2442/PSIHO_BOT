from peewee import *
from config_.conf import Configurator

conf = Configurator()
pg_db = PostgresqlDatabase(host=conf.db_conf.host,
                           port=conf.db_conf.port,
                           database=conf.db_conf.db_name,
                           user=conf.db_conf.user,
                           password=conf.db_conf.user_pass,
                           )


class BaseDbModel(Model):
    class Meta:
        database = pg_db


class Statuses(BaseDbModel):
    descr = CharField()
    action = CharField(null=True)


class TgClient(BaseDbModel):
    tg_id = IntegerField()
    status = ForeignKeyField(Statuses)
    first_name = CharField(null=True)
    last_name = CharField(null=True)
    username = CharField(null=True)


class Menu(BaseDbModel):
    descr = CharField()
    status = ForeignKeyField(Statuses, on_delete="CASCADE", null=True)


class TextAnswers(BaseDbModel):
    question = TextField()
    answer = TextField()


class MenuButton(BaseDbModel):
    menu_id = ForeignKeyField(Menu, on_delete="CASCADE", null=True)
    text = CharField()
    answer = TextField()
    to_status = ForeignKeyField(Statuses, on_delete="CASCADE", null=True)
    set_action = CharField(null=True)


class Commands(BaseDbModel):
    text = CharField()
    answer = TextField()
    to_status = ForeignKeyField(Statuses, on_delete="CASCADE", null=True)


class AdminUser(BaseDbModel):
    name = CharField()
    email = CharField()
    password = CharField()
    token = CharField()


class AnswersStatistic(BaseDbModel):
    tg_user_id = IntegerField()
    datetime = DateTimeField()
    question = TextField()
    answer = TextField(null=True)


class Moderation(BaseDbModel):
    question = TextField()
    answer = TextField()
    accepted = BooleanField()
    deleted = BooleanField()
    author = TextField()


class NotifyTask(BaseDbModel):
    notify = TextField()
    deferre_time = DateTimeField()
    status = TextField(default="pending")
    message = TextField(default="Пока тут пусто")
