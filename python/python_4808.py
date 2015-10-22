# form.is_valid() always returning false
if request.method == 'POST':
   form = TransactionForm(user=request.user, data=request.POST)
