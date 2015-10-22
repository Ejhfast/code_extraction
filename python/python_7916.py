# How can I determine the current event in Google Calendar using Python?
events = client.events().list(calendarId='primary',
                              timeMin='2011-12-22T09:00:00Z',
                              timeMax='2011-12-22T22:00:00Z').execute()
