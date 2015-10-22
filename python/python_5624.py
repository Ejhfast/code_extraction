# How to make this python script memory efficient
docs_to_dump = Document.objects.all().order_by('court').iterator()
