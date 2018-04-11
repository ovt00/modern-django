from .base import *

SECRET_KEY = env('DJANGO_SECRET_KEY', default='!i+66np(&mvtndk$aq@v%6_q$@2!2*&)b%zf0i+r-1^@e62_di')

DEBUG = env.bool('DJANGO_DEBUG', True)
