from .base import *

DEBUG = True

"""
production settings
"""
import os
from dotenv import load_dotenv
from .base import *

load_dotenv(os.path.join(BASE_DIR,".env"))

SECRET_KEY = os.getenv("SECRET_KEY")

DEBUG = os.getenv("DEBUG")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.getenv("DB_NAME"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PWD"),
        "HOST": os.getenv("DB_HOST"),
        "PORT": os.getenv("DB_PORT"),
    }

}
INSTALLED_APPS += [
    
]