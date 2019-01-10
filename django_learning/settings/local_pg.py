from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django_learning',
        'USER': 'django_learning',
        'PASSWORD': 'django_learning',
        'HOST': '127.0.0.1',
        'PORT': '5432'
    }
}
