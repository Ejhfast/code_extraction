# Django: Most efficient way to link two elements in different tables
author = request.user
Review.objects.filter(chapter__work__user=author)
