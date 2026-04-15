"""Django settings — minimal, development-only."""
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
SECRET_KEY = "chartexa-dev-secret-change-in-production"
DEBUG = True
ALLOWED_HOSTS = ["*"]
INSTALLED_APPS = [
    "django.contrib.staticfiles",
    "cx_dashboard",
]
TEMPLATES = [{
    "BACKEND": "django.template.backends.django.DjangoTemplates",
    "DIRS": [BASE_DIR / "cx_dashboard" / "templates"],
    "OPTIONS": {"context_processors": []},
}]
ROOT_URLCONF = "urls"
STATIC_URL = "/static/"
