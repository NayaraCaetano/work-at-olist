from .base import *

import dj_database_url

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', '.herokuapp.com']

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)


CELERY_REMAP_SIGTERM = 'SIGQUIT celery -A calls_bill_project worker -l info'
CELERY_DEFAULT_QUEUE = 'work-at-olist-celery'
CELERY_BROKER_TRANSPORT_OPTIONS['queue_name_prefix'] = 'work-at-olist-'
