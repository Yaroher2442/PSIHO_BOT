import peewee
from database.models import pg_db, Statuses, TgClient, Menu, TextAnswers, MenuButton, Commands, AdminUser, \
    AnswersStatistic, Moderation

if __name__ == '__main__':
    pg_db.create_tables([Statuses, TgClient, Menu, TextAnswers, MenuButton, Commands, AdminUser, AnswersStatistic, Moderation])
