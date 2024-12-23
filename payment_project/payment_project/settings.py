from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-0ip4kh^54ff3whazp12^41q=k%(jflnwl)3kvq0-1x!d-**=zv'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["senseistrategypayment.com", "www.senseistrategypayment.com"]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'payment_app',  # Bu satırı ekleyin
    'corsheaders',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'payment_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'payment_project.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = '/static/'

# Static files için
STATICFILES_DIRS = [
    BASE_DIR / "payment_app/static",  # veya uygun bir yol
]

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CORS_ALLOWED_ORIGINS = [
    "https://www.senseistrategypayment.com",
    "https://senseistrategypayment.com",
]

CSRF_TRUSTED_ORIGINS = [
    "https://www.senseistrategypayment.com",
    "https://senseistrategypayment.com",
]
CORS_ALLOW_CREDENTIALS = True

# settings.py
SECURE_SSL_REDIRECT = True  # Tüm HTTP isteklerini HTTPS'e yönlendirir
SESSION_COOKIE_SECURE = True  # Çerezlerin yalnızca HTTPS üzerinden gönderilmesini sağlar
CSRF_COOKIE_SECURE = True  # CSRF çerezinin yalnızca HTTPS üzerinden gönderilmesini sağlar
SECURE_HSTS_SECONDS = 31536000  # HSTS (HTTP Strict Transport Security) için süre (1 yıl)
SECURE_HSTS_INCLUDE_SUBDOMAINS = True  # Alt domainleri HSTS'ye dahil eder
SECURE_HSTS_PRELOAD = True  # HSTS preload listesi için işaretler
SECURE_CONTENT_TYPE_NOSNIFF = True  # Tarayıcıların içeriği yanlış şekilde yorumlamasını engeller
SECURE_BROWSER_XSS_FILTER = True  # XSS (Cross-Site Scripting) saldırılarına karşı koruma sağlar
