# Can't make null value for DateTimeProperty
{{ i.date_posted.strftime('%d %b %Y')  if i.date_posted != None  }}
