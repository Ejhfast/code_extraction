# Replacing object_list with ListView: AttributeError
view = ListView.as_view(template_name='generic_list.html')
return view(request, *args, **kwargs)
