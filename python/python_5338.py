# Filtering the drop down list of ReferenceModels created by appengine using django
def __init__(self, *args, **kwargs):
    super(SecondForm, self).__init__(*args, **kwargs)
    self.fields['first'].query = db.Query(First).fetch(10)
