"""
Django settings for susdormAdmin project.

Generated by 'django-admin startproject' using Django 4.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os

from .csrf import CsrfExemptSessionAuthentication

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-_o2mg8m2gb83!k(veb#m7lwb@d6fnsx39!s3lb**_vten_#zgr'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['8.138.105.61', '127.0.0.1', 'www.susdorm.top']


# Application definition

INSTALLED_APPS = [
    'simpleui',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'account',
    'dorm',
    'mptt',
    'django_oss_storage',
    'import_export',
    'rest_framework',
    'api',
    'corsheaders',
    'taggit',
    'taggit_serializer'
]

# 更改默认语言为中文
LANGUAGE_CODE = 'zh-hans'

SIMPLEUI_HOME_INFO = False 
SIMPLEUI_ANALYSIS = False 

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware'
]

CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
    'https://oop-project-copy.vercel.app',
    'https://susdorm.online',
    'https://www.susdorm.online'
]
CORS_ALLOW_CREDENTIALS = True

CORS_ALLOW_HEADERS = ('content-disposition', 'accept-encoding',
                      'content-type', 'accept', 'origin', 'authorization','sessionid', 'Cookie', 'Access-Control-Allow-Origin')

SIMPLEUI_LOGO = "https://backend.susdorm.online/static/logo.jpg"

# rest framework
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        # 'rest_framework.authentication.SessionAuthentication',
        'susdormAdmin.csrf.CsrfExemptSessionAuthentication',
        'rest_framework.authentication.BasicAuthentication'
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    # 'PAGE_SIZE': 10,
}

ROOT_URLCONF = 'susdormAdmin.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            'templates'
        ],
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

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

# SESSION_ENGINE = "django.contrib.sessions.backends.cache"
# SESSION_CACHE_ALIAS = "default"

WSGI_APPLICATION = 'susdormAdmin.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',   # 数据库引擎
#         'NAME': 'susdorm',  # 数据库名，先前创建的
#         'USER': 'root',     # 用户名，可以自己创建用户
#         'PASSWORD': 'Susdorm2023',  # 密码
#         'HOST': '127.0.0.1',  # mysql服务所在的主机ip
#         'PORT': '3306',         # mysql服务端口
#     }
# }

DATABASES = {  
    'default': {  
        'ENGINE': 'django.db.backends.sqlite3',  
        'NAME': BASE_DIR / 'db.sqlite3',  
    }  
}

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static/")


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

REST_PASSWORD_VALIDATORS = [
    {
        'NAME': 'api.utils.validators.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'api.utils.validators.MinimumLengthValidator',
    },
    {
        'NAME': 'api.utils.validators.CommonPasswordValidator',
    },
    {
        'NAME': 'api.utils.validators.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# 下面配置阿里云oss对象储存服务
OSS_ACCESS_KEY_ID = ""
OSS_ACCESS_KEY_SECRET = ""
# OSS_ENDPOINT = "oss-cn-hangzhou.aliyuncs.com"    # 访问域名, 根据服务器上的实际配置修改
OSS_ENDPOINT = "oss-cn-shenzhen.aliyuncs.com"
OSS_BUCKET_NAME = ""    # oss 创建的 BUCKET 名称
BUCKET_ACL_TYPE = "public-read"
# BUCKET_ACL_TYPE = "private"
DEFAULT_FILE_STORAGE = 'django_oss_storage.backends.OssMediaStorage'
