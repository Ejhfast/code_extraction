# django prevent delete of model instance
problematic_field = models.ForeignKey(ActualTableModel, on_delete=models.PROTECT)
