# Django query: Want to count a set in template
count = models.StorageItem.objects.filter(client=client_id, itemstatushistory__isnull=False).count()
