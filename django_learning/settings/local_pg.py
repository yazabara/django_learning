from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django_learning',
        'USER': 'django_learning',
        'PASSWORD': 'django_learning',
        'HOST': 'workout-portal-api-db',
        'PORT': '5432'
    }
}
