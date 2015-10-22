# Error when extend on_change method in invoice_line
res = super(account_invoice_line, self).product_id_change(product, uom_id, qty=0, name='', type_x='out_invoice',partner_id=False, fposition_id=False, price_unit=False, currency_id=False,
company_id=None)
