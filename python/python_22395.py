# Django: Make all Error (404, 500, etc.) URLs fallback to parent URL
# urls.py
from some.file.views import My404View
handler404 = My404View.as_view()
