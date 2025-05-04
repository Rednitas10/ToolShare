# backend/tool_rental/wsgi.py
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tool_rental.settings")
application = get_wsgi_application()
