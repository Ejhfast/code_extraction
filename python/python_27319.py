# django widget as argument
def __init__(self, *args, **kwargs):
     super(YourForm, self).__init__(*args, **kwargs)
     self.fields['password'].widget.attrs['class'] = 'classname'
