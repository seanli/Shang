from settings import *

ENVIRONMENT = 'PROD'

ALLOWED_HOSTS = [
    'shang.herokuapp.com',
    'shang.li',
    'www.shang.li'
]

DEBUG = False
TEMPLATE_DEBUG = DEBUG

DATABASES = {'default': dj_database_url.config(default='postgres://localhost')}

STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_STORAGE_BUCKET_NAME = 'shang-li'
AWS_S3_FILE_OVERWRITE = True
AWS_QUERYSTRING_AUTH = False
AWS_HEADERS = {
    'Cache-Control': 'public, max-age=%s' % (30 * 24 * 60 * 60),
}
COMPRESS_STORAGE = STATICFILES_STORAGE

STATIC_URL = 'https://s3.amazonaws.com/shang-li/'
MEDIA_URL = 'https://s3.amazonaws.com/shang-li/'

# AWS Information
AWS_ACCESS_KEY_ID = 'AKIAIWUXQY7UILQNXKDA'
AWS_SECRET_ACCESS_KEY = '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'

# Raven Information
RAVEN_CONFIG = {
    'dsn': 'https://2c00eae32e2143f082722d9c746b6c0d:162025fd37754f6e88d428efd7caed8b@app.getsentry.com/11109',
}
