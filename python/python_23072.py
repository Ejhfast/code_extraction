# Printing Multiple Variables of a Python Class
attrs = ['make', 'model', 'year', 'color']
print " ".join(map(lambda attr: getattr(car1, attr), attrs))
