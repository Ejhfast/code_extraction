# Django remove unicode in values_list
definitions_list = [definition.encode("utf8") for definition in definitions.objects.values_list('title', flat=True)]
