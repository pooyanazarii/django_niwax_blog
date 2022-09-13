from bniwax_pj.settings import *
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-6snfu*%89j#y91jf^@cy^*_1d+7*8l33&dfcr5cd7v5c7%l42m'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["*"]

# INSTALLED_APPS =[]

#site map config
SITE_ID = 2

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# STATIC_ROOT = BASE_DIR /'static'
MEDIA_ROOT = BASE_DIR /'media'

STATICFILES_DIRS  = [
    BASE_DIR / 'static',
]


# CSRF_COOKIE_SECURE = True