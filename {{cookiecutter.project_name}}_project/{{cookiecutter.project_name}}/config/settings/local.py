from .base import *
from .apps import INSTALLED_APPS

INSTALLED_APPS += [
    'debug_toolbar'
]

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

# SQLite
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, '{{cookiecutter.project_name}}.sqlite3'),
#     }
# }

# PostgreSQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get(
            '{{cookiecutter.project_name|upper}}_DB_NAME',
            '{{cookiecutter.project_name}}'),
        'USER': os.environ.get(
            '{{cookiecutter.project_name|upper}}_DB_USERNAME',
            '{{cookiecutter.project_name}}'),
        'PASSWORD': os.environ.get(
            '{{cookiecutter.project_name|upper}}_DB_PASS',
            '{{cookiecutter.project_name}}'),
        'HOST': os.environ.get(
            '{{cookiecutter.project_name|upper}}_DB_HOST', 'localhost'),
        'PORT': os.environ.get(
            '{{cookiecutter.project_name|upper}}_DB_PORT', '')
    }
}
