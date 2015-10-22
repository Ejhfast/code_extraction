# In Django, how do I select 100 random records from the database?
Content.objects.all().order_by('?')[:100]
