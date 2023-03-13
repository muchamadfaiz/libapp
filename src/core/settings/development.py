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
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

INSTALLED_APPS += [
    
]