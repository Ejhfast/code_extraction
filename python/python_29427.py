# Django default value date and time when form opens up
def __init__(self, *args, **kwargs):
    super(TransactionForm, self).__init__(*args, **kwargs)
    self.fields['trans_date'].initial = #pre populated field.
