# OpenERP 7 How to null check?
emp_no = no_define_object_no and no_define_object_no[0].current_no or False
return {'value': {'emp_no':  emp_no}}
