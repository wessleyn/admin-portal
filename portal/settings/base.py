from pathlib import Path
from os import name

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

INSTALLED_APPS = [

    # SetUp
    # 'setup.apps.SetupConfig',

    # External
    "phonenumber_field",
    'fontawesomefree',
    'dal',
    'dal_select2',
    'rest_framework',
    # 'grappelli',
    

    # My Own
    'apps.teacher',
    'apps.classroom.apps.ClassroomConfig',
    'apps.student.apps.StudentConfig',
    'apps.hod.apps.HodConfig',
    'apps.adminstrator',
    'apps.dean.apps.DeanConfig',
    'apps.school.apps.SchoolConfig',


    # Default
    # 'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',

    # Database
    'psycopg'
]
# The directory seperator used when traversing dirs 
DIR_SEP = '//' if name == 'posix' else '\\' 

MIDDLEWARE = [

    # Default 
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

ROOT_URLCONF = 'portal.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates/'],
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

WSGI_APPLICATION = 'portal.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
}

FIXTURE_DIRS =[ BASE_DIR / '.data/']

LOGIN_URL = 'login'

LOGIN_REDIRECT_URL = 'dashboard'

LOGOUT_REDIRECT_URL = 'home'

AUTHENTICATION_BACKENDS =[
    # Default
    "django.contrib.auth.backends.ModelBackend",

    # Authenticating site users
    "apps.student.backends.StudentLoginBackend",
    "apps.dean.backends.DeanLoginBackend"
]

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Harare'

USE_I18N = True

USE_TZ = True

STATICFILES_DIRS = [
    BASE_DIR / ".static/"
]


STATIC_URL = 'static/'

MEDIA_ROOT = BASE_DIR / '.media'

MEDIA_URL = '/.media/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_HOST = 'sandbox.smtp.mailtrap.io'

EMAIL_HOST_USER = '75bba00cfa7188'

EMAIL_HOST_PASSWORD = '7eb6bc28020e87'

EMAIL_PORT = '2525'
