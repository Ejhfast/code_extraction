# How can I join 3 tables and output all three together joined in web2py?
db((db.course.id == db.files.course_id) &amp; (db.dept.id==db.course.dept_id))
