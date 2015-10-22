# Want to Add all amounts for each country
uk_sales = Sale.objects.filter(country_type='1')
uk_amount = uk_sales.aggregate(price = Sum('amount'))['price']
