# merge two lists in equal amounts
lt = l1[:max(5, 10 - len(l2))] + l2[:max(5, 10 - len(l1))]
