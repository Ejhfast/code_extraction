# simplest way to return a new list by remove index/value from another list? (order required)
(x for x in o1 if x not in value)
(x for i, x in enumerate( o1 ) if i not in index )
