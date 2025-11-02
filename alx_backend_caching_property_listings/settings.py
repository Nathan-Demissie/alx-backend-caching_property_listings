DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'property_db',
        'USER': 'user',
        'PASSWORD': 'password',
        'HOST': 'db',  # Matches the service name in docker-compose.yml
        'PORT': '5432',
    }
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://redis:6379/1",  # Matches Redis service name
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

INSTALLED_APPS = [
    ...
    'properties',
    'django_redis',
]

TIME_ZONE = 'Africa/Addis_Ababa'
USE_TZ = True
