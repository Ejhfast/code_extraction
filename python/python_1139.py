# Correct way to access related objects
employees = Employee.objects.filter(id=your_id).select_related()
if employees.count() == 1:
    phone_numbers = employees[0].phonenumber_set.all()
