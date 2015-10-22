# How do i cast char to integer while querying in django ORM?
students.objects.filter(student_id__contains="97318") \
                .extra({'stident_id_uint': "CAST(student_id as UNSIGNED)"}) \
                .order_by('-student_id_uint')
