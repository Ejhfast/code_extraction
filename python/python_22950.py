# Django accessing foreign key value from api
student_detail = Student.objects.filter(last_name=pk, campus__name=pk2)
