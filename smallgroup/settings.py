"""
Django settings for smallgroup project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'y1#x-0b98+5nnoz8z)s@y4bmzug=-lh^(9fxzga0jh8%(v(eku'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['lhousehold.pythonanywhere.com']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'sgroups',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'smallgroup.urls'

WSGI_APPLICATION = 'smallgroup.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
#}

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
#        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'lhousehold$smallgroup',
        'USER': 'lhousehold',
        'PASSWORD': '918bathurst',
        'HOST': 'mysql.server',
    }
}

#SOUTH_DATABASE_ADAPTERS = {
#    'default' : 'south.db.mysql'
#}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = '/home/lhousehold/smallgroup/static/'

MEDIA_URL = '/media/'

MEDIA_ROOT = '/home/lhousehold/smallgroup/media/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
    '/var/www/static/',
)

MEDIAFILES_DIRS = (
    os.path.join(BASE_DIR, "media"),
    '/var/www/media/',
)


EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'connect.central.ctf@gmail.com'
EMAIL_HOST_PASSWORD = '89bathurst'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
