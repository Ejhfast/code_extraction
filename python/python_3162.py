# Django / Python, Make database save function re-usable (so that it takes modelname and appname from strings), using contenttypes or some other method?
instancemodelname = ContentType.objects.get(app_label="myappname", model="mymodelname")
b = instancemodelname.model_class()(account_username='testtestest')
b.save()
