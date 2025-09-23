from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

import json, os

# load secret config if exists
secret_path = os.path.join(BASE_DIR, '.secret_config', 'secret.json')
if os.path.exists(secret_path):
    with open(secret_path) as f:
        secrets = json.load(f)
else:
    secrets = {}

SECRET_KEY = secrets.get('DJANGO_SECRET_KEY', 'django-insecure-test-key')
DEBUG = True
ALLOWED_HOSTS = []

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

CUSTOM_APPS = [
    'todo',
    'users',
]

THIRD_PARTY_APPS = [
    'django_extensions',
    'django_summernote',
    'django_cleanup',
]

INSTALLED_APPS = DJANGO_APPS + CUSTOM_APPS + THIRD_PARTY_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = []

LANGUAGE_CODE = 'ko-kr'
TIME_ZONE = 'Asia/Seoul'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SUMMERNOTE_CONFIG = {
    'iframe': True,
    'summernote': {
        'airMode': False,
        'width': '100%',
        'height': '480',
        'toolbar': [
            ['style', ['style']],
            ['font', ['bold', 'underline', 'clear']],
            ['color', ['color']],
            ['para', ['ul', 'ol', 'paragraph']],
            ['table', ['table']],
            ['insert', ['link', 'picture']],
            ['view', ['fullscreen']],
        ],
        'lang': 'ko-KR',
        'codemirror': {
            'mode': 'htmlmixed',
            'lineNumbers': 'true',
            'theme': 'monokai',
        },
    },
    'attachment_require_authentication': True,
    'disable_attachment': False,
    'attachment_absolute_uri': True,
}

# Custom user model
AUTH_USER_MODEL = 'users.User'

# Email settings from secret.json (development)
EMAIL_HOST = secrets.get('EMAIL_HOST', 'localhost')
EMAIL_PORT = secrets.get('EMAIL_PORT', 25)
EMAIL_HOST_USER = secrets.get('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = secrets.get('EMAIL_HOST_PASSWORD', '')
EMAIL_USE_TLS = secrets.get('EMAIL_USE_TLS', False)


# Email settings for verification
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = SECRET.get('EMAIL', {}).get('USER')
EMAIL_HOST_PASSWORD = SECRET.get('EMAIL', {}).get('PASSWORD')
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
