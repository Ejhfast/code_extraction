# django cannot multiply non-int of type 'str'
def _total_amount(self):
    req = QuoteRow.objects.filter(quote=self.pk)
    return sum([i.unit_price * i.quantity for i in req])
