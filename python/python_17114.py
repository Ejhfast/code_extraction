# push notification using Django
@receiver(post_save, sender=MyModel)
def my_handler(sender, **kwargs):
    ...
