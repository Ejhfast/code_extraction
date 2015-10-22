# Printing formatted arbitrary precision decimals in python
&gt;&gt;&gt; import decimal
&gt;&gt;&gt; '{0:.2f}'.format(decimal.Decimal((pow(2,70)-2)))
1180591620717411303422.00
