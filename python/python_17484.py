# Sorting numerically get order as 1,2,3 not 1, 10, 11, 12 in Django Python
myQuery.filter().extra(
    select={'myinteger': 'CAST(mycharfield AS UNSIGNED)'}
).order_by('myinteger')
