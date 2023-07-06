import os
from random import randint
from statsig import statsig, StatsigUser
from flask import Flask

statsig.initialize("secret-I9RZAyjyxdffBKd8B5Q9N9lYsTw0e1eo91uYqlOhmSU")

app = Flask(__name__)


@app.route('/')
def root():
    user = StatsigUser(user_id=f"user-{randint(1, 1000)}")
    config = statsig.get_config(user, 'a_config')
    return {"version": config.get('version'), "pid": os.getpid()}


if __name__ == '__main__':
    app.run()
