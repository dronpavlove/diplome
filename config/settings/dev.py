from .base import *  # noqa: F403

DEBUG = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        }
    },
    'formatters': {
        'default': {
            'format': '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]',
        },
    },
    'handlers': {
        'debug-console': {
            'class': 'logging.StreamHandler',
            'formatter': 'default',
            'filters': ['require_debug_true'],
        },
    },
    # django.db.backends - выводит запросы в БД
    'loggers': {
        # 'django.db.backends': {
        #     'level': 'DEBUG',
        #     'handlers': ['debug-console'],
        #     'propagate': False,
        # }
    },
}

INSTALLED_APPS.append('debug_toolbar')  # noqa: F405
INSTALLED_APPS.append('django_extensions')  # noqa: F405
INSTALLED_APPS.append('fixturemedia')  # noqa: F405

MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware')  # noqa: F405
#
try:
    INTERNAL_IPS.append('127.0.0.1')  # noqa: F405
except Exception:
    INTERNAL_IPS = [
        '127.0.0.1',
    ]

DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK": lambda request: True,
}
