# Django, can I get reference objects included with a queryset
for item_due in ItemDue.objects.filter(some_criteria).select_related():
    print item_due.item.ref_id
