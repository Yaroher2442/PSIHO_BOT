import threading

from flask import Flask
from flask.logging import default_handler
from flask_cors import CORS
from admin.views import *
from config.loger import AppLogger
import logging


class AdminApp(threading.Thread):
    app = Flask(__name__, static_url_path=''
                , static_folder="static")
    CORS(app)

    def __init__(self, conf):
        threading.Thread.__init__(self)
        self.logger = AppLogger("admin", conf)
        self.log = logging.getLogger('werkzeug')
        for handl in self.logger.handlers:
            self.log.addHandler(handl)
        self.register_api()

        @self.app.errorhandler(404)
        def page_not_found(e):
            # note that we set the 404 status explicitly
            return render_template('helpers/404.html'), 404

        @self.app.errorhandler(500)
        def page_not_found(e):
            # note that we set the 404 status explicitly
            return render_template('helpers/500.html'), 500

    def register_api(self):
        self.app.add_url_rule('/index', view_func=Index.as_view('index'))

        self.app.add_url_rule('/register', view_func=Register.as_view('register'))
        self.app.add_url_rule('/login', view_func=Login.as_view('login'))
        self.app.add_url_rule('/logout', view_func=Logout.as_view('logout'))

        self.app.add_url_rule('/bots', view_func=Bots.as_view('bots'))

        self.app.add_url_rule('/menus', view_func=Menus.as_view('menus'))
        self.app.add_url_rule('/buttons', view_func=Buttons.as_view('buttons'))
        self.app.add_url_rule('/texts', view_func=Texts.as_view('texts'))

        self.app.add_url_rule('/statistic', view_func=Menus.as_view('statistic'))

    def run(self):
        self.app.run(debug=False)
