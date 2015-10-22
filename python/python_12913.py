# Create new object using concatenated strings as object name
attendees = {}
newObjectName = fName[0] + lName
attendees[newObjectName] = Attendee(fName, lName, email)
