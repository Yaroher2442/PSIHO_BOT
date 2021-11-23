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

conf = Configurator()
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


if __name__ == '__main__':
    if migrate():
        threads = []

        gunicorn_options = {
            'bind': f'{conf.server_conf.host}:5000',
            'workers': 1
        }
        wsgi_app = AdminApp(conf).app.wsgi_app

        workers = [TGBot(conf)]
        for wrkr in workers:
            wrkr.setDaemon(True)
            wrkr.start()
            app_logger.info(f"Thread {wrkr} start")
            threads.append(wrkr)

        GunicornApp(wsgi_app, gunicorn_options).run()
        # while True:
        #     for w in workers:
        #         if not w.is_alive():
        #             w.start()
        #             app_logger.info(f"Thread {w} reload")
        #         else:
        #             continue
    else:
        app_logger.critical("Migrations not set, exit")
        exit(-1)
