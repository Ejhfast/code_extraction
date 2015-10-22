# Django queries on properties of related object sets
Teacher.objects.exclude(Q(students__absent=False) | Q(students=None))
