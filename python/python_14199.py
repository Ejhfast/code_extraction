# queryset = Evento.objects.filter(Q(mod__isnull=True, aprobado=True) | Q(mod__isnull=False, mod__activo=False))
