# WTForms creating a custom widget
def __init__(self, label=None, validators=None, text='Save', **kwargs):
    super(InlineButton, self).__init__(label, validators, **kwargs)
    self.text = text
