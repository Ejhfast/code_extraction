# Make a single insert query in python
sql = "INSERT INTO tbltemplate (template_name) VALUES (%s)"
for template in dir_template_list:
    conn.query(sql, (template,))
