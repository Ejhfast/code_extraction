# Paginated based on the alphabet (A-Z)
pages = [myQuerySet.filter(myfield__istartswith=i) for i in "ABC...XYZ"] #full alphabet here
