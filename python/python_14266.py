# Best way to detect floating round off error in python
&gt;&gt;&gt; from decimal import Decimal
&gt;&gt;&gt; Decimal(0.35)
Decimal('0.34999999999999997779553950749686919152736663818359375')
