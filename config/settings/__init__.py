"""
Settings module initialization.
Automatically loads the correct settings based on DJANGO_ENV variable.
"""

import os

# Determine which settings to use
env = os.environ.get('DJANGO_ENV', 'dev')

if env == 'prod':
    from .prod import *
else:
    from .dev import *