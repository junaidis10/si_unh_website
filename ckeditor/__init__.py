"""
Shim for django-ckeditor when the package is not installed.
Provides RichTextField as a plain TextField so the project can run
without the real ckeditor dependency.
"""
from django.db import models


class RichTextField(models.TextField):
    """Drop-in replacement that falls back to a plain TextField."""
    pass
