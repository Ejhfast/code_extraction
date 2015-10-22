# Merge QuerySetValues object in Django
categories=CategoryAnswers.objects.values('category', 'brand').distinct()
for cat in categories:
    print CategoryAnswers.objects.filter(category=cat["category"], brand=cat["brand"]).values('category', 'brand').annotate(total=Sum('answer'))
