# Can Django ORM do an ORDER BY on a specific value of a column?
q = Ticket.objects.extra(select={'is_top': "status = 4"})
q = q.extra(order_by = ['-is_top'])
