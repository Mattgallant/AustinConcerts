"""
Django settings for austin_data_bass project.

Generated by 'django-admin startproject' using Django 3.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'v!_^w+2fms1a+qp^&!ood@uxzo%p_d8*tobr&029-^q!v7*qz_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'austindatabass.appspot.com',]


# Application definition

INSTALLED_APPS = [
    'webapp.apps.WebappConfig',
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

ROOT_URLCONF = 'austin_data_bass.urls'

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

WSGI_APPLICATION = 'austin_data_bass.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
      'ENGINE': 'django.db.backends.postgresql',
      #'HOST': '/cloudsql/djangopractice-272319:us-central1:djangopractice-dbs',
      'HOST': '34.68.27.7',
      'PORT': '5432', # PostgreSQL port
      'NAME': 'test',
      'USER': 'dbuser', # either 'postgres' (default) or one you created on the PostgreSQL instance page
      'PASSWORD': 'password2'
    }
}

'''DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}'''


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
# /static/ if DEBUG else Google Cloud bucket url

STATIC_URL = '/static/' # T and F works locally
#STATIC_URL = 'webapp/static/' #T no, F yes
#STATIC_URL = '/webapp/static/' # T and F works locally
#STATIC_URL = os.path.join(BASE_DIR, 'webapp/static/') #both no
#STATIC_URL =  os.path.join(os.path.dirname(BASE_DIR), 'austindatabass-bucket/') #both no

# this is the url that you sync static files to
# link to bucket for static files
# server error
#STATIC_URL: 'https://storage.googleapis.com/austindatabass-bucket/static/' #T cmd error, F server error
#STATIC_URL: 'https://storage.googleapis.com/austindatabass-bucket/' #T cmd error, F server error


# collectstatic directory (located OUTSIDE the base directory)
# TODO: configure the name and path to your static bucket directory (where collectstatic will copy to)
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'austindatabass-bucket') # destination location

STATICFILES_DIRS = [
  # TODO: configure the name and path to your development static directory
    #os.path.join(BASE_DIR, 'static'), # static directory (in the top level directory) for local testing
    os.path.join(BASE_DIR, 'webapp/static/'), # from this location
]

# to sync static files to bucket. go to static root level then:
# gsutil rsync -r austindatabass-bucket gs://austindatabass-bucket/static

# for bucket permission, after every sync
# gsutil acl -r ch -u AllUsers:R gs://austindatabass-bucket/static