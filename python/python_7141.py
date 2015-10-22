# how to use "where in" clause
News.objects.filter(created_by__agency_position__id=your_agency_id)[:5]
