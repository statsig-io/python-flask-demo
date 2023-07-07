from random import randint
from flask import Flask
from statsig import statsig, StatsigUser

import os
import gunicorn.app.base


class StandaloneApplication(gunicorn.app.base.BaseApplication):

    def init(self, parser, opts, args):
        pass

    def __init__(self, app, options=None):
        self.options = options or {}
        self.application = app
        super().__init__()

    def load_config(self):
        config = {key: value for key, value in self.options.items()
                  if key in self.cfg.settings and value is not None}
        for key, value in config.items():
            self.cfg.set(key.lower(), value)

    def load(self):
        statsig.initialize("secret-I9RZAyjyxdffBKd8B5Q9N9lYsTw0e1eo91uYqlOhmSU")
        return self.application


if __name__ == '__main__':
    app = Flask(__name__)


    @app.route('/')
    def root():
        user = StatsigUser(user_id=f"user-{randint(1, 1000)}")
        config = statsig.get_config(user, 'a_config')
        return {"version": config.get('version'), "pid": os.getpid()}


    options = {
        'bind': '127.0.0.1:8000',
        'workers': 4,
    }

    StandaloneApplication(app, options).run()
