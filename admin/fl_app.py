from flask import Flask
from flask_cors import CORS
from config.conf import Configurator
from admin.views import *


class FL_CLI:
    conf = Configurator()
    app = Flask(__name__, static_folder="admin")
    CORS(app)

    def __init__(self):
        self.register_api()

    def register_api(self):
        self.app.add_url_rule('/', view_func=Index.as_view('index'))
        self.app.add_url_rule('/register', view_func=Register.as_view('register'))
        self.app.add_url_rule('/login', view_func=Login.as_view('login'))

    def run(self):
        self.app.run()


if __name__ == '__main__':
    FL_CLI().run()
