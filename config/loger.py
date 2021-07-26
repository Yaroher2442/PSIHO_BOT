import logging
from logging.handlers import TimedRotatingFileHandler
from config.conf import Configurator
import os
from colorlog import ColoredFormatter


class AppLogger(logging.Logger):
    def __init__(self, loger_name, conf):
        logging.Logger.__init__(self, name=loger_name)
        self.stream_handler = logging.StreamHandler()
        self.formatter = ColoredFormatter('%(log_color)s%(asctime)s | %(name)s - %(levelname)s - %(message)s')
        self.stream_handler.setFormatter(self.formatter)
        self.rotate = TimedRotatingFileHandler(os.path.join(conf.base_path, "logs", f'{loger_name}.log'),
                                               when=conf.log_conf.when,
                                               interval=conf.log_conf.interval)
        self.rotate.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))

        self.handlers.append(self.stream_handler)
        self.handlers.append(self.rotate)
