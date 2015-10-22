# Searching from multiple models (jquery autocomplete)
m1 = M1.objects.filter(title__istartswith=q)
m2 = M2.objects.filter(title__istartswith=q)
results = [x.title for x in m1] + [x.title for x in m2]
