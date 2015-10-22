# Django - Join 2 Models in Query
Phone.objects.filter(number=u'945678987', person__employer=u'xyz')
