# Django search in the database
pattern= r"\b%s\b" % text
Product.objects.filter(name__regex = pattern)
