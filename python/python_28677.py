# How to filter objects on datetime fields?
announcements = Announcement.objects.all().filter(date_start__gte = datetime.now())
