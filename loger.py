import logging

class log_creator(logging.Logger):
    def __init__(self, loger_name,log_file):
        logging.Logger.__init__(self, name=loger_name)
        self.stream_handler = logging.StreamHandler()
        self.stream_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        self.handlers.append(self.stream_handler)
        self.handler = logging.FileHandler(log_file)
        self.format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.handler.setFormatter(self.format)
        self.handlers.append(self.handler)
