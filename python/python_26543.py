# Django rest-framework howto serialize a objetc/foreign key
data = JSONParser().parse(request)
data.update({'pk': project_id})
