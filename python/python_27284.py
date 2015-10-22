# Most python(3)esque way to repeatedly SELECT from MySQL database
crm_ids = ",".join(customers)
select_customer = "SELECT UNIQUE id FROM customers WHERE CRM_id IN (%s);" % crm_ids
