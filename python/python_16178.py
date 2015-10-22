# how to create a downloadable csv file in appengine
self.response.headers['Content-Type'] = 'application/csv'
writer = csv.writer(self.response.out)
writer.writerow(['foo','foo,bar', 'bar'])
