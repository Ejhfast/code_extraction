# ArcGIS: accessing python list output from listFields geoprocessor
sFields = gp.ListFields(linktofeatureclass)
for field in sFields:
    print field.Name, field.Type, field.Scale
