# Better way to add constant column to pandas data frame
testdf['avg_sales_per_sku'] = testdf.sales.sum() / testdf.skus.sum()
