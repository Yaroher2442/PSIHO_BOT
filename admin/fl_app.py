import threading

from flask import Flask
from flask.logging import default_handler
from flask_cors import CORS
from telegram.ext import ExtBot
from werkzeug.middleware.dispatcher import DispatcherMiddleware

import config_.conf
from admin.views import *
from config_.loger import AppLogger
import logging

from gunicorn.app.base import BaseApplication


class AdminApp():
    app = Flask(__name__, static_url_path=''
                , static_folder="static")

    CORS(app)

    def __init__(self, conf: config_.conf.Configurator, bot: ExtBot):
        # self.app.config["APPLICATION_ROOT"] = conf.server_conf.base_url
        self.app.wsgi_app = DispatcherMiddleware(
            Response('Not Found', status=404),
            {conf.server_conf.base_url: self.app.wsgi_app}
        )
        self.bot = bot
        self.config = conf
        self.logger = AppLogger("admin", self.config)
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
        self.app.add_url_rule('/', view_func=Index.as_view('index'))

        self.app.add_url_rule('/register', view_func=Register.as_view('register'))
        self.app.add_url_rule('/login', view_func=Login.as_view('login'))
        self.app.add_url_rule('/logout', view_func=Logout.as_view('logout'))

        self.app.add_url_rule('/menus', view_func=Menus.as_view('menus'))
        self.app.add_url_rule('/buttons', view_func=Buttons.as_view('buttons'))
        self.app.add_url_rule('/texts', view_func=Texts.as_view('texts'))
        self.app.add_url_rule('/commands', view_func=Commands.as_view('commands'))
        self.app.add_url_rule('/moderations', view_func=Moderation.as_view('moderations'))
        self.app.add_url_rule('/request_answer', view_func=UserModerPage.as_view('usermoder'))
        self.app.add_url_rule('/delete/<table>/<item_id>', view_func=Delete.as_view('delete'))
        self.app.add_url_rule('/aprove_moderation/<item_id>', view_func=AproveModeration.as_view("aprove"))
        self.app.add_url_rule('/statistic', view_func=Statistic.as_view('statistic'))

        NotificationsPage.tg_bot = self.bot

        self.app.add_url_rule('/notifications', view_func=NotificationsPage.as_view('notifications'))

    # def run(self):
    #     self.app.run(host=self.config.server_conf.host, port=self.config.server_conf.port,
    #                  debug=self.config.server_conf.debug, reloader_interval=50)


class GunicornApp(BaseApplication):
    def __init__(self, app, options=None):
        self.options = options or {}
        self.application = app
        super(GunicornApp, self).__init__()

    def load_config(self):
        config = {
            key: value for key, value in self.options.items()
            if key in self.cfg.settings and value is not None
        }
        for key, value in config.items():
            self.cfg.set(key.lower(), value)

    def load(self):
        return self.application
