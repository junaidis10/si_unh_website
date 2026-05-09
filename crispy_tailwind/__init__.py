"""Shim for crispy_tailwind when not installed."""
from django.apps import AppConfig

class CrispyTailwindConfig(AppConfig):
    name = 'crispy_tailwind'
    verbose_name = 'Crispy Tailwind (shim)'

default_app_config = 'crispy_tailwind.CrispyTailwindConfig'
