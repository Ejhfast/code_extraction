# Django and weird legacy database tables
def names_for(product_id):
    return [row.namestring for row in ProductName.objects.filter(product_id=product_id)]
