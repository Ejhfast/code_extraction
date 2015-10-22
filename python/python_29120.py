# Django get multiple latest elements using filter
all_pages = Page.objects.all()
revision_ids = [p.revisions.order_by('-created').first().pk for p in all_pages]
page_revisions = PageRevision.objects.filter(pk__in=revision_ids)
