# Django: Two or more filters in django queryset
get_meetings = Meeting.objects.filter(created_by = user_id.id, date_created__lte = datetime.date.today())[index:limit]
