"""
Django settings for Blog project.

Generated by 'django-admin startproject' using Django 2.1.

For more information on this file, see
https://docs.djangoproject.com/en/{{ docs_version }}/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/
"""

import os

from .environment import env


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def rel(*path):
    return os.path.join(BASE_DIR, *path)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/{{ docs_version }}/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("BLOG_DEBUG")

ALLOWED_HOSTS = env.list("BLOG_ALLOWED_HOSTS", default=[])

SECRET_KEY = env.str("BLOG_SECRET_KEY")

# Application definition

INSTALLED_APPS = [
    # django apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # 3rd party apps
    "rest_framework",
    # our apps
    "Blog.apps.common.apps.CommonConfig",
    "Blog.apps.account.apps.AccountConfig",
    "Blog.apps.blog.apps.BlogConfig"
] + env.list("BLOG_DEV_INSTALLED_APPS", default=[])

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
] + env.list("BLOG_DEV_MIDDLEWARE", default=[])

ROOT_URLCONF = "Blog.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [rel("templates/")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

WSGI_APPLICATION = "Blog.wsgi.application"


# Database
# https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#databases

DATABASES = {"default": env.db("BLOG_DATABASE_URL")}


# Password validation
# https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#auth-password-validators

AUTH_USER_MODEL = "account.User"

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

SESSION_COOKIE_SECURE = env.bool("BLOG_SESSION_COOKIE_SECURE", default=True)
SESSION_COOKIE_NAME = "s"
CSRF_COOKIE_NAME = "c"


# Internationalization
# https://docs.djangoproject.com/en/{{ docs_version }}/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/{{ docs_version }}/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = rel("staticfiles/")
STATICFILES_DIRS = (rel("static/"),)

MEDIA_URL = "/media/"
MEDIA_ROOT = rel("media/")
