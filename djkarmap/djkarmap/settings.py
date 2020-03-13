"""
Django settings for djkarmap project.

Generated by 'django-admin startproject' using Django 3.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# add spatial libarary
# TODO add this setting as environment variable in production 
GDAL_LIBRARY_PATH = "D:/poje/koocho_projects/karmap/venv/Lib/site-packages/osgeo/gdal300.dll"
GEOS_LIBRARY_PATH = "D:/poje/koocho_projects/karmap/venv/Lib/site-packages/osgeo/geos_c.dll"

GDAL_DATA = "D:/poje/koocho_projects/karmap/venv/Lib/site-packages/osgeo/data/gdal"
PROJ_LIB = "D:/poje/koocho_projects/karmap/venv/Lib/site-packages/osgeo/data/proj"

os.environ['GDAL_DATA'] = GDAL_DATA
os.environ['PROJ_LIB'] = PROJ_LIB
path = "D:/poje/koocho_projects/karmap/venv/Lib\site-packages/osgeo;"
os.environ['PATH'] = path + os.environ['PATH']



# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '9306h&il)nfd+ox@@juj0j2n^2)fcxq_b6m#ob^)jw1=pe=_4r'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 3rd Party
    'crispy_forms',
    # Project apps
    'django.contrib.gis',
    'accounts',
    'main_app',
    'pages',
    
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

ROOT_URLCONF = 'djkarmap.urls'

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

WSGI_APPLICATION = 'djkarmap.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'djkarmap_db',                      
        'USER': 'postgres',
        'PASSWORD': '123456789',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


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

LANGUAGE_CODE = 'fa' #'en-us'

TIME_ZONE = 'Asia/Tehran' # 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

# customize default django User auth
AUTH_USER_MODEL = 'accounts.CustomUser'
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'

# we’re using Bootstrap4 so we should tell this to crispy form.
# activate Django template cache loader
# TODO In production environments, always activate Django template cache loader.
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# for password reset email backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'