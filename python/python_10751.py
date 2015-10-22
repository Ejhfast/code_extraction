# How to filter data (queryset) in django admin interface by string length?
qs = Code.objects.extra(where=['CHAR_LENGTH(code_key) = 10'])
