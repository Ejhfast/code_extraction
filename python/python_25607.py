# getting multiple values out of an SQL statement
cursor.execute("select Count(TeacherID) from TeacherInfo where TeacherInitials = ?",(TeacherInitials,))
