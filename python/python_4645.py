# A better way than eval() when translating keyword arguments in QuerySets (Python/Django)
q = Q(**{"categories__slug_" + current_lang + "__contains": slug})
items = Items.objects.filter(q)
