# Django: Is there a way to have the "through" model in a ManyToManyField in a different app to the model containing the ManyToManyField?
class Car(models.Model):
    manufacturer = models.ForeignKey('production.Manufacturer')
