"""
Django settings for Kickcard project.
"""

import os
from pathlib import Path

# ========================
# BASE DIR
# ========================
BASE_DIR = Path(__file__).resolve().parent.parent


# ========================
# SECURITY
# ========================
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-temp-key')

DEBUG = False

ALLOWED_HOSTS = ['*']  # change after deployment


# ========================
# CUSTOM USER MODEL
# ========================
AUTH_USER_MODEL = 'Card.user'


# ========================
# APPLICATIONS
# ========================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'Card',
]


# ========================
# MIDDLEWARE
# ========================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # IMPORTANT
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# ========================
# URL CONFIG
# ========================
ROOT_URLCONF = 'Kickcard.urls'


# ========================
# TEMPLATES
# ========================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # ✅ your structure
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


# ========================
# WSGI
# ========================
WSGI_APPLICATION = 'Kickcard.wsgi.application'


# ========================
# DATABASE (SQLITE OK)
# ========================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# ========================
# PASSWORD VALIDATION
# ========================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# ========================
# INTERNATIONALIZATION
# ========================
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# ========================
# STATIC FILES (CRITICAL)
# ========================
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')  # ✅ your static folder
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # required for deploy

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# ========================
# DEFAULT FIELD
# ========================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# ========================
# CSRF (FOR RENDER)
# ========================
CSRF_TRUSTED_ORIGINS = [
    'https://kickcard.onrender.com'
]