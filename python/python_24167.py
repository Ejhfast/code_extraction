# How to get current ID record in a domain field in OpenERP7?
&lt;field name="main_contact_id" domain="[('parent_id', '=', context.get('active_id', False))]"/&gt;
