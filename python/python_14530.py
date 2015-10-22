# Get all fields from model that are of specific type in django
for field in self.fields:
    if isinstance(field, forms.IntegerField):
        field.widget.attrs['class'] = 'biggerWidth'
