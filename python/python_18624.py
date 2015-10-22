# File attachment path issue in CSV with django
response = HttpResponse(mimetype='text/csv')
response['Content-Disposition'] = 'attachment; filename=unruly.csv'
writer = csv.writer(response)
