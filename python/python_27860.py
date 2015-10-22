# Max and one-to-many and one-to-one relationship
max_value = Model3.objects.filter(model2__model1=self).aggregate(Max('value'))
