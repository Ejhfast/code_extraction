# Django filter by datetime, after converting string to datetime
compute_usages = ComputeUsages.objects.filter(customer_id = customer_id).filter(values_date = datetime(year, day, selected_month))
