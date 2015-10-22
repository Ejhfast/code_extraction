# Search multiple field form data in mysql database with python
sql = "select * from PERSON where (F_Name = '%s' or L_Name = '%s' or Age = '%s') and Gender = '%s';"
self.cursor.execute(sql % (self.fname, self.lname, self.age, self.gender))
