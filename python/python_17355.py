# Django date format issue - does not match format
newdate = datetime.datetime.strptime(str(mydate), '%Y-%m-%d').strftime('%m/%Y')
