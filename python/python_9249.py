# Initialize django model capturing a derivative attribute from that moment
def __init__(self, *args, **kwargs):
    super(YourModel, self).__init__(*args, **kwargs)
    self.impact = self.user.get_profile().someIntField
