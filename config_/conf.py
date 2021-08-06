import json
import os


class Configurator():
    def __init__(self):
        self.base_path = os.getcwd()
        try:
            with open(os.path.join(self.base_path, "config_", "config.json")) as conf_file:
                self.json_conf = dict(json.load(conf_file))
        except:
            with open(os.path.join(self.base_path, "..", 'config_', "config.json")) as conf_file:
                self.json_conf = dict(json.load(conf_file))
        self.tg_conf = TG_config(**self.json_conf['telegram'])
        self.db_conf = DB_config(**self.json_conf['database'])
        self.log_conf = LOG_config(**self.json_conf["logger"])


class TG_config:
    def __init__(self, **kwargs):
        self.token = None
        for k, v in kwargs.items():
            setattr(self, k, v)


class DB_config:
    def __init__(self, **kwargs):
        self.host = None
        self.port = None
        self.user = None
        self.user_pass = None
        self.db_name = None
        for k, v in kwargs.items():
            setattr(self, k, v)


class LOG_config:
    def __init__(self, **kwargs):
        self.when = None
        self.interval = None
        for k, v in kwargs.items():
            setattr(self, k, v)


if __name__ == '__main__':
    conf = Configurator()
