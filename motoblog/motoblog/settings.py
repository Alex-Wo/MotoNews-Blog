import os
from pathlib import Path

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# Build paths inside the project like this: BASE_DIR / 'subdir'.

BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = (os.getenv('SECRET_KEY'))

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = (os.getenv('DEBUG'))

ALLOWED_HOSTS = ['*']

# Настроечный параметр для идентификации сайта

SITE_ID = 1

# Application definition

INSTALLED_APPS = [
    'blog.apps.BlogConfig',
    'taggit',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.postgres',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'motoblog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'motoblog.wsgi.application'

# Databases

DATABASES = {
    'default': {
        'ENGINE': (os.getenv('ENGINE')),
        'NAME': (os.getenv('NAME')),
        'USER': (os.getenv('USER')),
        'PASSWORD': (os.getenv('PASSWORD')),
        'HOST': (os.getenv('HOST')),
        'PORT': (os.getenv('PORT')),
    }
}

# Password validation

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization

LANGUAGE_CODE = (os.getenv('LANGUAGE_CODE'))

TIME_ZONE = (os.getenv('TIME_ZONE'))

USE_I18N = (os.getenv('USE_I18N'))

USE_TZ = (os.getenv('USE_TZ'))

# Static files (CSS, JavaScript, Images)

STATIC_URL = (os.getenv('STATIC_URL'))

# Default primary key field type

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Sending emails

EMAIL_HOST = (os.getenv('EMAIL_HOST'))
EMAIL_HOST_USER = (os.getenv('EMAIL_HOST_USER'))
EMAIL_HOST_PASSWORD = (os.getenv('EMAIL_HOST_PASSWORD'))
EMAIL_PORT = (os.getenv('EMAIL_PORT'))
EMAIL_USE_TLS = (os.getenv('EMAIL_USE_TLS'))
