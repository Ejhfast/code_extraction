# Get a foreign key field when using values and annotate
top_donors_month = Donation.objects.values('donator__first_name').annotate(Sum('amount')).order_by('-amount__sum').filter(datafilter)
top_donors_all = Donation.objects.values('donator__first_name').annotate(Sum('amount')).order_by('-amount__sum')
