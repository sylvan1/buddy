import os

# This is ~/workspace/buddy
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SECRET_KEY = 'y9!*o5s1r+chuu^wy97t3h2i0-$ojvn9*4dzgl9s5%v$s0i6-('
DEBUG = False

ALLOWED_HOSTS = []
DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

THIRD_PARTY_APPS = (
    'crispy_forms',  # Form layouts
    'allauth',  # registration
    'allauth.account',  # registration
    'allauth.socialaccount',  # registration
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.github',
)

BUDDY_APPS = (
    'users',
    'projects',
    'utils',
)

AUTOCOMPLETE_APP = ( # Must be before 'django.contrib.admin'
    'dal',
    'dal_select2',
)

INSTALLED_APPS = AUTOCOMPLETE_APP + DJANGO_APPS + THIRD_PARTY_APPS + BUDDY_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

SITE_ID = 1

MIGRATION_MODULES = {
    'sites': 'contrib.sites.migrations'
}

ROOT_URLCONF = 'urls'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            'templates',
        ],

        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
                'django.core.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'wsgi.application'
DATABASES = {
    'default': {
        'ENGINE': 'to_be_configured',
        'NAME': 'to_be_configured',
    }
}

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
AUTH_USER_MODEL = 'users.User'

ACCOUNT_ADAPTER = 'users.adapters.AccountAdapter'
SOCIALACCOUNT_ADAPTER = 'users.adapters.SocialAccountAdapter'
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': ['profile', 'email'],
        'AUTH_PARAMS': {'access_type': 'online'}
    },
    'facebook': {
        'METHOD': 'js_sdk',  # 'oauth2',
        'SCOPE': ['email', 'public_profile', 'user_friends'],
        # 'AUTH_PARAMS': {'auth_type': 'reauthenticate'},  # Should we always ask for password?
        'FIELDS': [
            'id',
            'email',
            'name',
            'first_name',
            'last_name',
            'verified',
            'locale',
            'timezone',
            'link',
            'gender',
            'updated_time'],
        'EXCHANGE_TOKEN': True,
        'LOCALE_FUNC': lambda request: 'en_US',
        'VERIFIED_EMAIL': False,
    },
    'github': {
        'SCOPE': ['user', 'email', 'repo'],
        'AUTH_PARAMS': {'access_type': 'online'},
        'METHOD': 'oauth',
    },
}

LOGIN_REDIRECT_URL = 'users:redirect'
LOGIN_URL = 'account_login'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
