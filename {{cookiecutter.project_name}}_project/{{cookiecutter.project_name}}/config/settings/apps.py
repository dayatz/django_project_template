# Application definition

DEFAULT_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# Your thirdparty apps listed here
THIRDPARTY_APPS = [
    'versatileimagefield',
]

# Your project apps listed here
PROJECT_APPS = [
    'core',
]
PROJECT_APPS = ['apps.%s' % (app) for app in PROJECT_APPS]

INSTALLED_APPS = DEFAULT_APPS + THIRDPARTY_APPS + PROJECT_APPS
