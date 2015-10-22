# Limiting results returned fromquery in django, python
User.objects.filter(is_active=True).order_by("-date_joined")[:10]
