# auto-generated snapshot
from peewee import *
import datetime
import peewee


snapshot = Snapshot()


@snapshot.append
class AdminUser(peewee.Model):
    name = CharField(max_length=255)
    email = CharField(max_length=255)
    password = CharField(max_length=255)
    token = CharField(max_length=255)
    class Meta:
        table_name = "adminuser"


@snapshot.append
class AnswersStatistic(peewee.Model):
    tg_user_id = IntegerField()
    datetime = DateTimeField()
    question = CharField(max_length=255)
    answer = CharField(max_length=255, null=True)
    class Meta:
        table_name = "answersstatistic"


@snapshot.append
class Statuses(peewee.Model):
    descr = CharField(max_length=255)
    action = CharField(max_length=255, null=True)
    class Meta:
        table_name = "statuses"


@snapshot.append
class Commands(peewee.Model):
    text = CharField(max_length=255)
    answer = CharField(max_length=255)
    to_status = snapshot.ForeignKeyField(index=True, model='statuses', null=True, on_delete='CASCADE')
    class Meta:
        table_name = "commands"


@snapshot.append
class Menu(peewee.Model):
    descr = CharField(max_length=255)
    status = snapshot.ForeignKeyField(index=True, model='statuses', null=True, on_delete='CASCADE')
    class Meta:
        table_name = "menu"


@snapshot.append
class MenuButton(peewee.Model):
    menu_id = snapshot.ForeignKeyField(index=True, model='menu', null=True, on_delete='CASCADE')
    text = CharField(max_length=255)
    answer = CharField(max_length=255)
    to_status = snapshot.ForeignKeyField(index=True, model='statuses', null=True, on_delete='CASCADE')
    set_action = CharField(max_length=255, null=True)
    class Meta:
        table_name = "menubutton"


@snapshot.append
class TextAnswers(peewee.Model):
    question = CharField(max_length=255)
    answer = CharField(max_length=255)
    class Meta:
        table_name = "textanswers"


@snapshot.append
class TgClient(peewee.Model):
    tg_id = IntegerField()
    status = snapshot.ForeignKeyField(index=True, model='statuses')
    first_name = CharField(max_length=255, null=True)
    last_name = CharField(max_length=255, null=True)
    username = CharField(max_length=255, null=True)
    class Meta:
        table_name = "tgclient"


def backward(old_orm, new_orm):
    tgclient = new_orm['tgclient']
    return [
        # Apply default value '' to the field tgclient.username
        tgclient.update({tgclient.username: ''}).where(tgclient.username.is_null(True)),
        # Apply default value '' to the field tgclient.first_name
        tgclient.update({tgclient.first_name: ''}).where(tgclient.first_name.is_null(True)),
        # Apply default value '' to the field tgclient.last_name
        tgclient.update({tgclient.last_name: ''}).where(tgclient.last_name.is_null(True)),
    ]