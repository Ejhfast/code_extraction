# Comparing date in sql with custom date
total_amount=frappe.db.sql("""SELECT SUM(sale.grand_total) FROM `tabSales Invoice` sale where sale.posting_date= %s """ % date1)
