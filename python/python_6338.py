# Cannot get object from queryset
self.content = re.sub(r'\[\[(.+)\]\]', lambda m: ADResource.objects.all().get(alias=m.group(1)).src.url, self.content)
