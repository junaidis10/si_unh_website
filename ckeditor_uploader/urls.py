"""
Shim for ckeditor_uploader.urls when django-ckeditor is not installed.
Provides empty urlpatterns so include('ckeditor_uploader.urls') doesn't crash.
"""
urlpatterns = []
