"""
Shim for ckeditor.fields when django-ckeditor is not installed.
"""
from django.db import models


class RichTextField(models.TextField):
    """Drop-in replacement that falls back to a plain TextField."""
    pass
