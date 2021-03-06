import os

from django.conf import settings
from django.core.wsgi import get_wsgi_application
from dotenv import load_dotenv

if not settings.DEBUG:
    project_folder = os.path.expanduser("~/isabot.pythonanywhere.com")
    load_dotenv(os.path.join(project_folder, ".env"))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

application = get_wsgi_application()
