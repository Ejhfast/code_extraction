# django reversion - revert related field to the same version
version.revision.revert()
sales = version.object.sales_set.all()
version.revision.revert()
