import os
from pathlib import Path
from decouple import config, Csv
from dotenv import load_dotenv


load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent
PROJECT_DIR = Path(__file__).resolve().parent


SECRET_KEY = 'django-insecure-)*%af@mr+8s@xkxm$-q$)_3qwuhtqtgzxwb!&q9@f@sb%d'

DEBUG = False

ALLOWED_HOSTS = ['.vercel.app', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'whitenoise.runserver_nostatic',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'item',
    'newsletter',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.project.urls'

WSGI_APPLICATION = 'core.project.wsgi.application'

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
# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'railway',
        'USER': 'postgres',
        'PASSWORD': 'xMFsaFOkCMyDLWZkqEnvQpcVhIQmqudr',
        'HOST': 'monorail.proxy.rlwy.net',
        'PORT': '43056',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


STATIC_URL = '/static/'

# Directory where static files are stored during development
STATICFILES_DIRS = [os.path.join(BASE_DIR, "project/static")]

# Directory where static files are collected to for production
STATIC_ROOT = "staticfiles"

# WhiteNoise configuration to serve static files
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR /'media/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'




#AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
#AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
#AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')
#AWS_STORAGE_SIGNATURE_NAME = config('AWS_STORAGE_SIGNATURE_NAME')
#AWS_S3_REGION_NAME = config('AWS_S3_REGION_NAME')
#AWS_S3_FILE_OVERWRITE = False
#AWS_DEFAULT_ACL = None
#AWS_S3_VERIFY = True
#DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
