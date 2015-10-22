# unsupported operand type(s) for *: 'NoneType' and 'Decimal'
eu_amount = (eu_sales.aggregate(price = Sum('amount'))['price']) or 0  * vat/100
