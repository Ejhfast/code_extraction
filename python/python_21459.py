# Exclude by object in queryset
pages = [page1, page2] # page1 and page2 are Page objects
Page.objects.filter(site=site).exclude(pk__in=[p.pk for p in pages])
