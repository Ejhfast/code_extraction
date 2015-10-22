# How to display a date_time field in jinja2 template? (flask)
class AppointmentUpdateForm(wtf.Form):
    start_time = wtforms.DateField('Start at', [wtforms.validators.required()], widget=DatePickerWidget())
    end_time = wtforms.DateField('End at', [wtforms.validators.required()], widget=DatePickerWidget())
