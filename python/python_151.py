# Cleaner way to query on a dynamic number of columns in Django?
cars = CarModel.objects.all()
for op in self.cleaned_data['options']:
    cars = cars.filter((op, True))
