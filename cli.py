import os

import sys

from loguru import logger

sys.path.append(os.getcwd())
print(sys.path)

from tg_bot.bot import TGBot
from admin.fl_app import AdminApp, GunicornApp
from config_.conf import Configurator
from config_.loger import AppLogger
from database.migration import makemigrations
from config_.conf import conf

app_logger = AppLogger("app", conf)


def change_dir(dir):
    def actual_decorator(func):
        def wrapper(*args, **kwargs):
            retval = os.getcwd()
            app_logger.debug("Current working directory %s" % os.getcwd())
            os.chdir(os.path.join(retval, dir))
            ret = func(*args, **kwargs)
            app_logger.debug("Directory changed successfully %s" % os.getcwd())
            os.chdir(retval)
            app_logger.debug("Current working directory %s" % os.getcwd())
            return ret

        return wrapper

    return actual_decorator


@change_dir(dir='database')
def migrate():
    try:
        return makemigrations(logger=app_logger)
    except TypeError as te:
        logger.debug(f"Migrations failed with {te} maby all data updated")


# migrate()
if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Get args')
    parser.add_argument('-c', dest="create_db", default=False,
                        help='To create database', type=bool)
    parser.add_argument('-m', dest="migrate", default=False,
                        help='To create database', type=bool)
    args = parser.parse_args()
    print(args)
    if args.create_db:
        from database.models import pg_db, Statuses, TgClient, Menu, TextAnswers, MenuButton, Commands, AdminUser, \
            AnswersStatistic, Moderation

        pg_db.create_tables(
            [Statuses, TgClient, Menu, TextAnswers, MenuButton, Commands, AdminUser, AnswersStatistic,
             Moderation])
        logger.debug("Models in database created")
        exit()
    if args.migrate:
        if not migrate():
            app_logger.critical("Migrations not set, exit")
            exit(-1)
        else:
            logger.debug("migrations aply")
    threads = []
    gunicorn_options = {
        'bind': f'{conf.server_conf.host}:{conf.server_conf.port}',
        'workers': 1
    }
    tg_bot = TGBot(conf)
    wsgi_app = AdminApp(conf,tg_bot.bot).app.wsgi_app
    workers = [tg_bot]
    for wrkr in workers:
        wrkr.setDaemon(True)
        wrkr.start()
        app_logger.info(f"Thread {wrkr} start")
        threads.append(wrkr)

    GunicornApp(wsgi_app, gunicorn_options).run()
