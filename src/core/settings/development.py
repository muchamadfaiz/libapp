from .base import *

DEBUG = True

"""
production settings
"""
import os
from dotenv import load_dotenv
from .base import *

load_dotenv(os.path.join(BASE_DIR,".env"))

SECRET_KEY = 'django-insecure-l6)_i#d(^(r!7ah0d!e-^cpjr3js8+hr0f_eiro#l4)n9q*)4v'

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

INSTALLED_APPS += [
    
]