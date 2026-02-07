"""
Django settings for NovaShop project.

Entorno: Desarrollo (MVP)
Django: 5.2.11
"""

from pathlib import Path


# ======================================================
# 📁 PATHS
# ======================================================
BASE_DIR = Path(__file__).resolve().parent.parent


# ======================================================
# 🔐 SEGURIDAD (DEV)
# ======================================================
SECRET_KEY = "django-insecure-cambia-esto-en-produccion"

DEBUG = True

ALLOWED_HOSTS: list[str] = []


# ======================================================
# 📦 APLICACIONES
# ======================================================
DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

LOCAL_APPS = [
    "sells",
    "inventory",
]

THIRD_PARTY_APPS: list[str] = []

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS


# ======================================================
# 🧩 MIDDLEWARE
# ======================================================
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# ======================================================
# 🌐 URLS / WSGI
# ======================================================
ROOT_URLCONF = "config.urls"

WSGI_APPLICATION = "config.wsgi.application"


# ======================================================
# 🧠 TEMPLATES
# ======================================================
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],  # opcional
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


# ======================================================
# 🗄️ BASE DE DATOS
# ======================================================
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# ======================================================
# 🔑 VALIDACIÓN DE CONTRASEÑAS
# ======================================================
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# ======================================================
# 🌍 INTERNACIONALIZACIÓN
# ======================================================
LANGUAGE_CODE = "es-co"

TIME_ZONE = "America/Bogota"

USE_I18N = True
USE_TZ = True


# ======================================================
# 🧾 ARCHIVOS ESTÁTICOS
# ======================================================
STATIC_URL = "static/"

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# STATIC_ROOT = BASE_DIR / "staticfiles"  # producción


# ======================================================
# 🆔 DEFAULT PK
# ======================================================
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
