# mongoengine reference field query
customer = Customers.objects(id=request.args.get("customer-reservation")).get()
data = Reservations.objects(restaurant=rest, customer=customer).all()
