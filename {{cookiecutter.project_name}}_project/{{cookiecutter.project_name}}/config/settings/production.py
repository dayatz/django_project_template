from .base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get(
            "{{cookiecutter.project_name|upper}}_DB_NAME",
            {{cookiecutter.project_name}}),
        'USER': os.environ.get(
            "{{cookiecutter.project_name|upper}}_DB_USERNAME",
            {{cookiecutter.project_name}}),
        'PASSWORD': os.environ.get(
            "{{cookiecutter.project_name|upper}}_DB_PASS",
            {{cookiecutter.project_name}}),
        'HOST': os.environ.get(
            "{{cookiecutter.project_name|upper}}_DB_HOST", 'localhost'),
        'PORT': os.environ.get(
            "{{cookiecutter.project_name|upper}}_DB_PORT", '')
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': os.path.join(os.environ.get(
                "{{cookiecutter.project_name|upper}}_LOG_DIR"),
                os.path.join(os.path.dirname(BASE_DIR), 'log.txt')),
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['file'],
            'level': 'WARNING',
            'propagate': True,
        },
    },
}
