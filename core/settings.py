
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



SECRET_KEY = 'yy_9$(9f_(gn*0gg_0@1v!3g^h^$jqi%5h2e38$f_m&gp_uujb'


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
    'store',
    'basket',
    'account',
    
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

ROOT_URLCONF = 'core.urls'

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
                'store.context_processors.categories',
                'basket.context_processors.basket',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': 'orcl',
        'USER': 'c##Nsanbaev',
        'PASSWORD': '123',
        'HOST': '',
        'PORT': '',
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

STATICFILES_DIRS = [
    os.path.join(BASE_DIR , "static" )
    
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media/')

AUTH_USER_MODEL = 'account.UserBase'
LOGIN_REDIRECT_URL = '/account/dashboard'
LOGIN_URL = '/account/login/'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'smtp.gmail.com'   
EMAIL_HOST_USER = 'nsanbaev.15@gmail.com'
EMAIL_HOST_PASSWORD = 'iuuoyafzqnqkjvra'
EMAIL_PORT = 587    
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
