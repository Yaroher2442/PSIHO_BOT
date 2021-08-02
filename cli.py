from tg_bot.bot import TGBot
from admin.fl_app import AdminApp
from config.conf import Configurator

if __name__ == '__main__':

    conf = Configurator()
    threads = []
    workers = [TGBot(conf)]
    for wrkr in workers:
        wrkr.setDaemon(True)
        wrkr.start()
        threads.append(wrkr)

    for th in threads:
        th.join()
