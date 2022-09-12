from .base import *

DEBUG = False

ADMINS = (
  ('shal5ho4', 'rcxsoor@gmail.com'),
)

ALLOWED_HOSTS = ['*']

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': 'educa',
    'USER': 'shal5ho4',
    'PASSWORD': '0507sebun',
  }
}
