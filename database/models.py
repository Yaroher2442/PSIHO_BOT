from peewee import *
from config.conf import Configurator

conf = Configurator()

pg_db = PostgresqlDatabase(host=conf.db_conf.host,
                           port=conf.db_conf.port,
                           database=conf.db_conf.db_name,
                           user=conf.db_conf.user,
                           password=conf.db_conf.user_pass,
                           )

db = PostgresqlDatabase('people.db')


# class Client(Model):
#     name = CharField()
#     birthday = DateField()

    # class Meta:
    #     database = db
