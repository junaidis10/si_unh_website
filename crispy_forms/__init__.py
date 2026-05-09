"""Shim for crispy_forms when not installed."""
from django.apps import AppConfig

class CrispyFormsConfig(AppConfig):
    name = 'crispy_forms'
    verbose_name = 'Crispy Forms (shim)'

default_app_config = 'crispy_forms.CrispyFormsConfig'
