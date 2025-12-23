INSTALLED_APPS = [
    'django.contrib.staticfiles',
    'academy',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
    },
]

STATIC_URL = '/static/'
