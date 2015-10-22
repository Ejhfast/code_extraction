# Django multiple model inheritance, django-push-notifications
class Device(models.Model):
    ...
    gcm_device = models.OneToOneField(GCMDevice)
