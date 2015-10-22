# How can I set Invitee in Google Calendar through Python?
event_audit=gdata.calendar.AttendeeStatus("http://schemas.google.com/g/2005#event.invited")
event.who.append(gdata.calendar.Who(email="xyz@pqr.com",rel="http://schemas.google.com/g/2005#event.invited"))
