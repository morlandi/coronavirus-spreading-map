import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '_+@%dy+odny0d6(iuuu47md35#mj8+lx5pc(0+0$b-wb(_sq+c'
DEBUG = False
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', ]

INSTALLED_APPS = [
    'main',
]

MIDDLEWARE = []
ROOT_URLCONF = 'main.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
            ],
        },
    },
]

WSGI_APPLICATION = 'main.wsgi.application'
DATABASES = {}

try:
    from .local_settings import *
    print('Local settings imported from file "local_settings.py"')
except ModuleNotFoundError:
    pass
