# Stop Django from creating migrations if the list of choices of a field changes
class ActivePlugin(models.Model):
    plugin_name = models.CharField(max_length=32, choices=get_active_plugins)
