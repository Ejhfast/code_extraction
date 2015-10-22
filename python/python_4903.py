# Generate a django queryset based on dict keys
reduce(operator.or_, Q(**{key + '__icontains': val}) for (key, val) in D.iteritems())
