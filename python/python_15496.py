# Django: postgres datetime ordering incorrect?
ordered = models.Study.objects.order_by('arrived', '-priority__priority')
