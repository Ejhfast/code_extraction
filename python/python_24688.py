# django MEDIA_ROOT and MEDIA_URL TEMPLATES
urlpatterns = [
      # ... the rest of your URLconf goes here ...
  ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
