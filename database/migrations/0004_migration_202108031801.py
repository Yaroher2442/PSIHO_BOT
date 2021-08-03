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
    answer = CharField(max_length=255)
    class Meta:
        table_name = "answersstatistic"


@snapshot.append
class Statuses(peewee.Model):
    descr = CharField(max_length=255)
    action = CharField(max_length=255, null=True)
    class Meta:
        table_name = "statuses"


@snapshot.append
class Menu(peewee.Model):
    descr = CharField(max_length=255)
    status = snapshot.ForeignKeyField(index=True, model='statuses', null=True, on_delete='CASCADE')
    class Meta:
        table_name = "menu"


@snapshot.append
class MenuButton(peewee.Model):
    menu_id = snapshot.ForeignKeyField(index=True, model='menu', on_delete='CASCADE')
    text = CharField(max_length=255)
    to_status = snapshot.ForeignKeyField(index=True, model='statuses', null=True, on_delete='CASCADE')
    set_action = CharField(max_length=255, null=True)
    class Meta:
        table_name = "menubutton"


@snapshot.append
class BtnAnswerStortage(peewee.Model):
    q_id = snapshot.ForeignKeyField(index=True, model='menubutton', on_delete='CASCADE')
    answer = CharField(max_length=255)
    class Meta:
        table_name = "btnanswerstortage"


@snapshot.append
class Commands(peewee.Model):
    text = CharField(max_length=255)
    to_status = snapshot.ForeignKeyField(index=True, model='statuses', null=True, on_delete='CASCADE')
    class Meta:
        table_name = "commands"


@snapshot.append
class CommandsAnswerStortage(peewee.Model):
    q_id = snapshot.ForeignKeyField(index=True, model='commands', on_delete='CASCADE')
    answer = CharField(max_length=255)
    class Meta:
        table_name = "commandsanswerstortage"


@snapshot.append
class TextAnswers(peewee.Model):
    question = CharField(max_length=255)
    class Meta:
        table_name = "textanswers"


@snapshot.append
class TextAnswerStortage(peewee.Model):
    q_id = snapshot.ForeignKeyField(index=True, model='textanswers', on_delete='CASCADE')
    answer = CharField(max_length=255)
    class Meta:
        table_name = "textanswerstortage"


@snapshot.append
class TgClient(peewee.Model):
    tg_id = IntegerField()
    status = snapshot.ForeignKeyField(index=True, model='statuses')
    first_name = CharField(max_length=255)
    last_name = CharField(max_length=255)
    username = CharField(max_length=255)
    class Meta:
        table_name = "tgclient"


def backward(old_orm, new_orm):
    statuses = new_orm['statuses']
    menubutton = new_orm['menubutton']
    return [
        # Apply default value '' to the field statuses.action
        statuses.update({statuses.action: ''}).where(statuses.action.is_null(True)),
        # Apply default value '' to the field menubutton.set_action
        menubutton.update({menubutton.set_action: ''}).where(menubutton.set_action.is_null(True)),
    ]
