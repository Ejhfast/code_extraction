# Using ExecuteBatch from Python on Google Calendars API
uri = self.calendar.GetAlternateLink().href
batch_uri = uri + u'/batch'
calendar_service.ExecuteBatch(request_feed, batch_uri)
