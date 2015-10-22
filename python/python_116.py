# Flattening one-to-many relationship in Django
my_book = Book.objects.get(pk=1)
all_ingredients = Ingredient.objects.filter(recipe__book=my_book)
