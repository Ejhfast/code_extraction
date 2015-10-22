# Django ORM Left Join With GROUP BY and SUM
User.objects.filter(user_type=type).values('id').annotate(total_time=Sum(useraction__time))
