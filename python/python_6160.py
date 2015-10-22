# How to order a Django QuerySet string property numerically?
ordered = (qs.extra(select={"order_column": "CONVERT(column, INTEGER)"})
           .order_by("order_column"))
