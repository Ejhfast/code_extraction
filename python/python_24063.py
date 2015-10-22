# Django manytomany relationship over 2 apps
class Client(Person):
   favorite_stores = models.ManyToManyField('store.Store')
   favorite_vendors = models.ManyToManyField(Vendor)
