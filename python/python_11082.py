# Why does `getattr` not support consecutive attribute retrievals?
getattr(getattr(a, "b"), "c")
