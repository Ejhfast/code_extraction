# how to update values in a DataFrame based on values in another DataFrame?
containers.drop('Quantity', axis = 1).\
           join(inventory.groupby('ContainerCode').sum(), \
                on = 'ContainerCode')
