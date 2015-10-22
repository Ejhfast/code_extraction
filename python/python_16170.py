# Django From Choices Tuple Concatnation
sites = [(s.site_code, s.site_code) for s in Site.objects.all().order_by('site_code')]
SITE_CHOICES = [('All', 'All')] + sites
