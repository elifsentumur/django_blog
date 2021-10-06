from .base import *

ALLOWED_HOSTS = []
# SECURITY WARNING: keep the secret key used in production secret!
DEBUG = True

AUTH_PASSWORD_VALIDATORS = [

]

DATABASES={
   'default':{
      'ENGINE':'django.db.backends.postgresql',
      'NAME': 'django_blog',
      'USER': 'postgres',
      'PASSWORD':'admin',
      'HOST': 'localhost',
      'PORT':'5432',
   }
}
