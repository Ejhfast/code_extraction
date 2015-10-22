# Django: How to get field value dynamically using custom template tags?
var = self.model.objects.get(site_id__exact=current_site.id)
context[self.varname] = var.__dict__[self.field]#this will get the field's value dynamically, which is what I was looking for
