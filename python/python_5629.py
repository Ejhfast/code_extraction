# appengine: parse a csv data in uploaded file
import csv
for row in csv.reader(self.request.POST['file']):
  # process row
