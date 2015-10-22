# Error in Decoding JSON with Python, exporting jqGrid
from django.core.urlresolvers import resolve
view_match = resolve('/json/test_day/4982/')
json_data = view_match.func(request,**view_match.kwargs).content
