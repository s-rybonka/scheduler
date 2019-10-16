"""
Django settings for scheduler project.

Generated by 'django-admin startproject' using Django 2.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import environ

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

env = environ.Env(
	DJANGO_DEBUG=(bool, False),
	DJANGO_SECRET_KEY=(str, 'CHANGEME!!!$eb_5&aw%k#wo@(z12wwq7)u*8^7!vta6'),
	DJANGO_ALLOWED_HOSTS=(list, ['*']),
	DJANGO_STATIC_ROOT=(str, 'staticfiles'),
	API_DOC_SCHEMA_TITLE=(str, ''),
	API_DOC_SCHEMA_DESCRIPTION=(str, ''),
	API_DOC_SCHEMA_AUTHOR_EMAIL=(str, ''),
	API_DOC_SCHEMA_AGREEMENT_URL=(str, ''),
	API_DOC_SCHEMA_LICENCE=(str, ''),
)

environ.Env.read_env()

SECRET_KEY = env('DJANGO_SECRET_KEY')

DEBUG = env('DJANGO_DEBUG')

ALLOWED_HOSTS = env('DJANGO_ALLOWED_HOSTS')

DJANGO_APPS = [
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
]

LOCAL_APPS = [

]

THIRD_PARTY_APPS = [
	'rest_framework',
	'drf_yasg',
	'django_extensions',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
	'django.middleware.security.SecurityMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'scheduler.urls'

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'scheduler.wsgi.application'

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
	}
}

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = env('DJANGO_STATIC_ROOT')
STATICFILES_DIRS = (
	[os.path.join(BASE_DIR, 'static') ]
)

# REST FRAMEWORK OPTIONS.

REST_FRAMEWORK = {
	'DEFAULT_RENDERER_CLASSES': (
		'rest_framework.renderers.JSONRenderer',
	),
	'DEFAULT_PARSER_CLASSES': (
		'rest_framework.parsers.JSONParser',
	),
	'TEST_REQUEST_DEFAULT_FORMAT': 'json',
}

# SWAGGER OPTIONS.

SWAGGER_SETTINGS = {
	'SECURITY_DEFINITIONS': None,
	'APIS_SORTER': 'alpha',
	'OPERATIONS_SORTER': 'alpha',
}

# REDOC OPTIONS.

REDOC_SETTINGS = {
	'EXPAND_RESPONSES': '200,201',
	'LAZY_RENDERING': True,
}

# API DOC SCHEMA OPTIONS.

API_DOC_SCHEMA_TITLE = env('API_DOC_SCHEMA_TITLE')
API_DOC_SCHEMA_DESCRIPTION = env('API_DOC_SCHEMA_DESCRIPTION')
API_DOC_SCHEMA_AUTHOR_EMAIL = env('API_DOC_SCHEMA_AUTHOR_EMAIL')
API_DOC_SCHEMA_AGREEMENT_URL = env('API_DOC_SCHEMA_AGREEMENT_URL')
API_DOC_SCHEMA_LICENCE = env('API_DOC_SCHEMA_AGREEMENT_URL')
