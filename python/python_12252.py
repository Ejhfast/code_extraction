# django database delete specific number of entries
Statusmessages.objects.filter(pk__in=Statusmessages.objects.filter(time__lt=date).values_list('pk')[:30000]).delete()
