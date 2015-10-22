# mysql select data for each value in array
final_list = []
for destination in destinations:
    final_list += YourCDRModel.objects.filter(area__in=destination).values_list('number', flat=True).order_by('?')[0:3]
