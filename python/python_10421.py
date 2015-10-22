# Django how to order by many to many occurences
from django.db.models import Count
most_common = Ingredient.objects.annotate(num_recipes=Count('recipe')).order_by('-num_recipes')[0]
print most_common.name
