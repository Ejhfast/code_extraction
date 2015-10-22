# How do I make this kind of Query in Django foreign key relationships?
addresses = Address.objects.filter(customer__creditcard__number = 'thenumber#')
