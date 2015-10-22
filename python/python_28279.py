# How to filter by field of field (multi level relationship) in django admin?
school_name = "your school name"
Students_in_school = Student.objects.filter(grade__school__name = school_name)
