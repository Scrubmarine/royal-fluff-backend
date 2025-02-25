from backend.settings import *
# Test settings used for GitHub Actions
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'test_grooming_db',
        'USER': 'test_admin',
        'PASSWORD': 'testpassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

DEBUG = True
TESTING = True