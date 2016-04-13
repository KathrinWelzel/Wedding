import os
import sys
from unipath import Path
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.utils.importlib import import_module

PROJECT_DIR = Path(__file__).parent

from decouple import config

import dj_database_url

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': dj_database_url.config(
      default = config('DATABASE_URL'))
}

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.sites',

    'bootcamp.activities',
    'bootcamp.articles',
    'bootcamp.userauth',
    'bootcamp.core',
    'bootcamp.feeds',
    'bootcamp.tweets',
    'bootcamp.questions',
    'bootcamp.search',
    'bootcamp.photos',
    'photologue',
    'sortedm2m',
    'taggit',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'bootcamp.urls'

WSGI_APPLICATION = 'bootcamp.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LANGUAGES = (
    ('en', 'English'),
    ('pt-br', 'Portuguese'),
    ('es', 'Spanish')
)

LOCALE_PATHS = (PROJECT_DIR.child('locale'), )

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_ROOT = PROJECT_DIR.parent.child('staticfiles')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    PROJECT_DIR.child('static'),
)

MEDIA_ROOT = PROJECT_DIR.parent.child('media')
MEDIA_URL = '/media/'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

from photologue import PHOTOLOGUE_APP_DIR

TEMPLATE_DIRS = (
    PROJECT_DIR.child('templates'),
    PHOTOLOGUE_APP_DIR,
)

LOGIN_URL = '/'
LOGIN_REDIRECT_URL = '/feeds/'

ALLOWED_SIGNUP_DOMAINS = ['*']

FILE_UPLOAD_TEMP_DIR = '/tmp/'
FILE_UPLOAD_PERMISSIONS = 644

SITE_ID = 1

# Default limit for gallery.latest
LATEST_LIMIT = getattr(settings,
    'PHOTOLOGUE_GALLERY_LATEST_LIMIT', None)

# max_length setting for the ImageModel ImageField
IMAGE_FIELD_MAX_LENGTH = getattr(settings,
    'PHOTOLOGUE_IMAGE_FIELD_MAX_LENGTH', 100)

# Path to sample image
SAMPLE_IMAGE_PATH = getattr(settings,
    'SAMPLE_IMAGE_PATH',
    os.path.join(os.path.dirname(__file__), 'res', 'sample.jpg'))

# Photologue image path relative to media root
PHOTOLOGUE_DIR = getattr(settings, 'PHOTOLOGUE_DIR', 'photologue')

# Look for user function to define file paths
PHOTOLOGUE_PATH = getattr(settings, 'PHOTOLOGUE_PATH', None)
if PHOTOLOGUE_PATH is not None:
    if callable(PHOTOLOGUE_PATH):
        get_storage_path = PHOTOLOGUE_PATH
    else:
        parts = PHOTOLOGUE_PATH.split('.')
        module_name = '.'.join(parts[:-1])
        module = import_module(module_name)
        get_storage_path = getattr(module, parts[-1])
else:
    def get_storage_path(instance, filename):
        return os.path.join(PHOTOLOGUE_DIR, 'photos', filename)

# Quality options for JPEG images
JPEG_QUALITY_CHOICES = (
    (30, _('Very Low')),
    (40, _('Low')),
    (50, _('Medium-Low')),
    (60, _('Medium')),
    (70, _('Medium-High')),
    (80, _('High')),
    (90, _('Very High')),
)

# choices for new crop_anchor field in Photo
CROP_ANCHOR_CHOICES = (
    ('top', _('Top')),
    ('right', _('Right')),
    ('bottom', _('Bottom')),
    ('left', _('Left')),
    ('center', _('Center (Default)')),
)

IMAGE_TRANSPOSE_CHOICES = (
    ('FLIP_LEFT_RIGHT', _('Flip left to right')),
    ('FLIP_TOP_BOTTOM', _('Flip top to bottom')),
    ('ROTATE_90', _('Rotate 90 degrees counter-clockwise')),
    ('ROTATE_270', _('Rotate 90 degrees clockwise')),
    ('ROTATE_180', _('Rotate 180 degrees')),
)

WATERMARK_STYLE_CHOICES = (
    ('tile', _('Tile')),
    ('scale', _('Scale')),
)

# LOGGING CONFIGURATION TODO Insert later on
# A logging configuration that writes log messages to the console.
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': True,
#     # Formatting of messages.
#     'formatters': {
#         # Don't need to show the time when logging to console.
#         'console': {
#             'format': '%(levelname)s %(name)s.%(funcName)s (%(lineno)d) %(message)s'
#         }
#     },
#     # The handlers decide what we should do with a logging message - do we email
#     # it, ditch it, or write it to a file?
#     'handlers': {
#         # Writing to console. Use only in dev.
#         'console': {
#             'level': 'DEBUG',
#             'class': 'logging.StreamHandler',
#             'formatter': 'console'
#         },
#         # Send logs to /dev/null.
#         'null': {
#             'level': 'DEBUG',
#             'class': 'logging.NullHandler',
#         },
#     },
#     # Loggers decide what is logged.
#     'loggers': {
#         '': {
#             # Default (suitable for dev) is to log to console.
#             'handlers': ['console'],
#             'level': 'INFO',
#             'propagate': False,
#         },
#         'photologue': {
#             # Default (suitable for dev) is to log to console.
#             'handlers': ['console'],
#             'level': 'DEBUG',
#             'propagate': False,
#         },
#         # logging of SQL statements. Default is to ditch them (send them to
#         # null). Note that this logger only works if DEBUG = True.
#         'django.db.backends': {
#             'handlers': ['null'],
#             'level': 'DEBUG',
#             'propagate': False,
#         },
#     }
# }
#
# # Don't display logging messages to console during unit test runs.
# if len(sys.argv) > 1 and sys.argv[1] == 'test':
#     LOGGING['loggers']['']['handlers'] = ['null']
#     LOGGING['loggers']['photologue']['handlers'] = ['null']
