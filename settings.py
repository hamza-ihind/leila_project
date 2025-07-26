### project/settings.py

import os
import dj_database_url

SECRET_KEY = os.environ.get("SECRET_KEY")

DEBUG = os.environ.get("DEBUG") != "False"

ALLOWED_HOSTS = [".vercel.app", ".now.sh"]

INSTALLED_APPS = [
    "whitenoise.runserver_nostatic"
     # Other apps ....
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    # other apps ...
]


DATABASES = {
    'default': dj_database_url.parse(
        os.environ.get("DATABASE_URL"),
        conn_max_age=600,
        conn_health_checks=True,
    )
}

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles", "static")