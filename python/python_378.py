# Select Distinct Years and Months for Django Archive Page
Posts.objects.filter(draft=False).dates('post_date','month',order='DESC')
