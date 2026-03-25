import os

from .base import *  # noqa: F403

DEBUG = False

# -----------------------
# DATABASE (prod)
# -----------------------
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
# STATIC & MEDIA (prod)
# -----------------------
# iDrive E2 (S3-compatible)
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = os.getenv("AWS_STORAGE_BUCKET_NAME")
AWS_S3_ENDPOINT_URL = normalize_s3_endpoint_url(os.getenv("AWS_S3_ENDPOINT_URL"))
AWS_S3_REGION_NAME = os.getenv("AWS_S3_REGION_NAME", "us-west-1")
AWS_DEFAULT_ACL = None
AWS_QUERYSTRING_AUTH = True
AWS_S3_FILE_OVERWRITE = False
AWS_LOCATION_MEDIA = "media"

STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
        "OPTIONS": {"location": AWS_LOCATION_MEDIA},
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}
