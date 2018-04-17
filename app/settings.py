import os
from decouple import config

ROOT = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)
AUTO_RELOAD = config('AUTO_RELOAD', default=False, cast=bool)
PORT = config('APP_DEFAULT_PORT', default=8888, cast=int)
HOST = config('APP_DEFAULT_HOST', default='127.0.0.1')

settings = {}
settings['debug'] = DEBUG

settings['autoreload'] = AUTO_RELOAD
settings['port'] = PORT
settings['host'] = HOST
settings['cookie_secret'] = 'your-cookie-secret'
settings['xsrf_cookies'] = False
