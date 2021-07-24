import logging
from logging.handlers import TimedRotatingFileHandler
from config.conf import Configurator

conf = Configurator()


class AppLogger(logging.Logger):
    def __init__(self, loger_name):
        logging.Logger.__init__(self, name=loger_name)
        self.stream_handler = logging.StreamHandler()
        self.stream_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        self.rotate = TimedRotatingFileHandler(f"../logs/{loger_name}.log", when=conf.log_conf.when,
                                               interval=conf.log_conf.interval)  # макс размер файла и макс кол-во хранимых файлов
        self.rotate.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))

        self.handlers.append(self.stream_handler)
        self.handlers.append(self.rotate)


if __name__ == '__main__':
    logger=AppLogger('test_loger')
    logger.error('print hui')