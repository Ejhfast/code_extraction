# Django Annotate Conditional
user_array = User.objects.filter(charge__due_date__lte=date).annotate(amount_due=Sum('charge__amount'))
