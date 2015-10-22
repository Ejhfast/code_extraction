# dynamic filter choice field in django
plant_number = django_filters.ChoiceFilter(choices=[[o.id, o.plant_number + " " + o.Manufacturer] for o in Plant.objects.all().order_by('IMS_plant')])
