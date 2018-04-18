import os
from decouple import config


ROOT = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)
AUTO_RELOAD = config('AUTO_RELOAD', default=False, cast=bool)
PORT = config('APP_DEFAULT_PORT', default=8888, cast=int)
HOST = config('APP_DEFAULT_HOST', default='127.0.0.1')


# Tornado settings

SETTINGS = {}
SETTINGS['debug'] = DEBUG

SETTINGS['autoreload'] = AUTO_RELOAD
SETTINGS['port'] = PORT
SETTINGS['host'] = HOST
SETTINGS['cookie_secret'] = 'your-cookie-secret'
SETTINGS['xsrf_cookies'] = False


# Database

default_dburl = 'sqlite:///'+os.path.join(BASE_DIR, 'db.sqlite3')
DATABASES = {
    'default': config('DATABASE_URL', default=default_dburl),
}
