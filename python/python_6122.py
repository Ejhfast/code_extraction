# Inner join from two not directly related models in Django
B.objects.filter(a__c__user=someuser).distinct().values('my_data')
