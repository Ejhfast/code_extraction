# Django Model filters
list_acciones=Accion.objects.filter(proyectos__id__in=ids_Proyecto)
