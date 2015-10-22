# Querying through several models
querysets = [cls.objects.filter(date=now) for cls in [Model1, Model2, Model3]]
