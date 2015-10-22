# How to create mongoengine filter query from fields listed as string rather DocumentFields
_query = {'Id__istartswith': value}
return Q(**_query)
