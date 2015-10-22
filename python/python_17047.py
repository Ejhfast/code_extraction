# Modify variable just in the Django admin but not in database
def __init__(self, *args, **kwargs):
    super(MyModelAdminForm, self).__init__(*args, **kwargs)
    self.fields['value'].value = self.instance.get_reverted_value()
