# django 1.7 order by related field error
tutteIn = MktIn.objects.all().order_by('id_squadra__nome', 'ruolo', '-ingaggio')
