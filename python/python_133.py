# Foreign key from one app into another in Django
class Car(models.Model):
    manufacturer = models.ForeignKey('production.Manufacturer')
