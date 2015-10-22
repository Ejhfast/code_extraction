# How can I get 'urlpatterns = __import__(<string_name>)' to work like a normal import statement?
urlpatterns = __import__(project_urls).whateversubmodule.urlpatterns
