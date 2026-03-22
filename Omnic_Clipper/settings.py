import os
from pathlib import Path
from datetime import timedelta
from dotenv import load_dotenv

# -----------------------
# BASE SETUP
# -----------------------
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(dotenv_path=BASE_DIR / ".env")


def normalize_s3_endpoint_url(url: str | None) -> str | None:
    """Boto3 requires a full URL with scheme; allow host-only values from .env."""
    if not url:
        return None
    url = url.strip()
    if not url:
        return None
    if "://" not in url:
        url = f"https://{url.lstrip('/')}"
    return url.rstrip("/")

SECRET_KEY = os.getenv("SECRET_KEY", "unsafe-dev-key")
DEBUG = False if os.getenv("DEBUG") == "False" else True
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "*").split(",")

# -----------------------
# APPLICATIONS
# -----------------------
INSTALLED_APPS = [
    # Django core
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # DRF & auth
    "rest_framework",
    "django_filters",
    "rest_framework.authtoken",
    "dj_rest_auth",
    "corsheaders",
    # Utilities
    "drf_spectacular",
    "drf_spectacular_sidecar",
    "django_cleanup.apps.CleanupConfig",
    "drf_standardized_errors",
    # Dependencies
    "ckeditor",
    # Custom apps
    "apps.service",
    "apps.blog",
    "apps.testimonial",
    "apps.product",
    "apps.crm",
    "apps.order",
    "apps.cms",
    "storages",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "corsheaders.middleware.CorsMiddleware",
]

ROOT_URLCONF = "Omnic_Clipper.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
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

WSGI_APPLICATION = "Omnic_Clipper.wsgi.application"

# -----------------------
# DATABASE
# -----------------------
if DEBUG:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.getenv("DB_NAME"),
            "USER": os.getenv("DB_USER"),
            "PASSWORD": os.getenv("DB_PASSWORD"),
            "HOST": os.getenv("DB_HOST"),
            "PORT": str(os.getenv("DB_PORT")),
        }
    }

# -----------------------
# PASSWORD VALIDATION
# -----------------------
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# -----------------------
# REST FRAMEWORK & JWT
# -----------------------
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": ("dj_rest_auth.jwt_auth.JWTCookieAuthentication",),
    "DEFAULT_RENDERER_CLASSES": ("rest_framework.renderers.JSONRenderer",),
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

REST_AUTH = {"USE_JWT": True, "JWT_AUTH_HTTPONLY": False}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=365),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": False,
    "ALGORITHM": "HS256",
    "SIGNING_KEY": SECRET_KEY,
    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "TOKEN_USER_CLASS": "rest_framework_simplejwt.models.TokenUser",
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
}

# -----------------------
# INTERNATIONALIZATION
# -----------------------
LANGUAGE_CODE = "en-us"
TIME_ZONE = "Asia/Dhaka"
USE_I18N = True
USE_TZ = True

# -----------------------
# STATIC & MEDIA FILES
# -----------------------

if not DEBUG:
    # iDrive E2 (S3-compatible) when production and DEBUG=False
    AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
    AWS_STORAGE_BUCKET_NAME = os.getenv("AWS_STORAGE_BUCKET_NAME")
    AWS_S3_ENDPOINT_URL = normalize_s3_endpoint_url(os.getenv("AWS_S3_ENDPOINT_URL"))
    AWS_S3_REGION_NAME = os.getenv("AWS_S3_REGION_NAME", "us-west-1")
    AWS_DEFAULT_ACL = None
    AWS_QUERYSTRING_AUTH = False
    AWS_S3_FILE_OVERWRITE = False
    AWS_S3_CUSTOM_DOMAIN = os.getenv("AWS_S3_CUSTOM_DOMAIN")

    AWS_LOCATION_STATIC = os.getenv("AWS_LOCATION_STATIC", "static")
    AWS_LOCATION_MEDIA = os.getenv("AWS_LOCATION_MEDIA", "media")

    STORAGES = {
        "default": {
            "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
            "OPTIONS": {"location": AWS_LOCATION_MEDIA},
        },
        "staticfiles": {
            "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
            "OPTIONS": {"location": AWS_LOCATION_STATIC},
        },
    }

    STATIC_URL = "/static/"
    MEDIA_URL = "/media/"
    STATICFILES_DIRS = [BASE_DIR / "static"]
else:
    # Local disk (developing  / DEBUG=True)
    STATIC_ROOT = BASE_DIR / "staticfiles"
    STORAGES = {
        "default": {"BACKEND": "django.core.files.storage.FileSystemStorage"},
        "staticfiles": {"BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage"},
    }
    STATIC_URL = "/static/"
    STATICFILES_DIRS = [BASE_DIR / "static"]
    MEDIA_URL = "/media/"
    MEDIA_ROOT = BASE_DIR / "media"

# -----------------------
# DEFAULT PRIMARY KEY
# -----------------------
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# -----------------------
# CORS
# -----------------------
CORS_ORIGIN_ALLOW_ALL = True

# -----------------------
# SPECTACULAR / API DOCS
# -----------------------
SPECTACULAR_SETTINGS = {
    "TITLE": "Omnic Clipper | API Documentation",
    "DESCRIPTION": "Visit /doc for API documentation",
    "VERSION": "0.0.1",
    "SERVE_INCLUDE_SCHEMA": False,
    "SCHEMA_PATH_PREFIX_TRIM": True,
    "CAMELIZE_NAMES": True,
    "POSTPROCESSING_HOOKS": [],
    "COMPONENT_SPLIT_REQUEST": True,
    "SWAGGER_UI_DIST": "SIDECAR",
    "SWAGGER_UI_FAVICON_HREF": "#",
    "REDOC_DIST": "SIDECAR",
    "SWAGGER_UI_SETTINGS": {
        "deepLinking": True,
        "persistAuthorization": True,
        "displayOperationId": True,
    },
}