# Update queryset attribute value without losing order on that attribute
for i, record in enumerate(qs):
    record.value = i
