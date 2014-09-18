import os
import sys
import django
from django.conf import settings

DJANGO_VERSION = float('.'.join([str(i) for i in django.VERSION[0:2]]))

DIR_NAME = os.path.dirname(__file__)
settings.configure(
    DEBUG=True,
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
        }
    },
    INSTALLED_APPS=(
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.admin',
        'cuser',
    ),
    ROOT_URLCONF='testss.CuserTestCase.urls',
    MIDDLEWARE_CLASSES = [
        'django.middleware.common.CommonMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'cuser.middleware.CuserMiddleware',
    ]
)

from django.test.simple import DjangoTestSuiteRunner

if DJANGO_VERSION >= 1.7:
    django.setup()


test_runner = DjangoTestSuiteRunner(verbosity=2)
failures = test_runner.run_tests(['cuser', ])

if failures:
    sys.exit(failures)
