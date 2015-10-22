# pulling data from date field in google app engine form
temp_var = datetime.strptime(cgi.escape(self.request.get('exam_date')),"%m/%d/%Y")
pledge_data.checkup_date = temp_var
