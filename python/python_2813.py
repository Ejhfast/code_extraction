# Django-models. Complex request to database
start_date = datetime.date(2005, 8, 9)
end_date = datetime.date(2005, 8, 11)
Model.objects.filter(name__icontains="hello").filter(date__range(start_date,end_date))
