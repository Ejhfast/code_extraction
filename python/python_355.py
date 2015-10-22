# Django Forms, set an initial value to request.user
form = JobRecordForm( {'supervisor':request.user} )
