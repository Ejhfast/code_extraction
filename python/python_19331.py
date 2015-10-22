# How to call method save() in a Django model class using attr string name?
full_attr_name = 'image_' + attr_name
if hasattr(self, full_attr_name):
    getattr(self, full_attr_name).save(filename, suf, save=False)
