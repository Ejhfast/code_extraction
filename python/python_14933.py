# Django Foreign key query
Appointment.objects.filter(patient__contact__uid=1234)
