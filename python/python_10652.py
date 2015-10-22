# How to make the objects.filter method to work with a Custom Model Field that takes in dictionaries - Django?
MyModel.objects.filter(options__regex=r'a : b')
MyModel.objects.filter(options__regex=r'.*c : d')
