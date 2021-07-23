import logging
from logging.handlers import TimedRotatingFileHandler
from config.conf import Configurator

TRFH = Configurator()


class log_creator(logging.Logger):
    def __init__(self, loger_name, log_file):
        logging.Logger.__init__(self, name=loger_name)
        self.stream_handler = logging.StreamHandler()
        self.stream_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        self.rotate = TimedRotatingFileHandler(log_file, when=TRFH.log_conf.when,
                                               interval=TRFH.log_conf.interval)  # макс размер файла и макс кол-во хранимых файлов
        self.rotate.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))

        self.handlers.append(self.stream_handler)
        self.handlers.append(self.rotate)