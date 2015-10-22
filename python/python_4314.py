# Retrieving a set of model objects that are indirectly related
ExitType.objects.filter(exits__stop__line=line).distinct()
