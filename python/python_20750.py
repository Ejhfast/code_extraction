# Django - Reference data from another model using a foreign key
tag_number = int(instrumentform.cleaned_data['tag'])
for query_result in Class1.objects.filter(tag = tag_number).values_list('example1', 'exmaple2'):
    example5, example6 = query_result
