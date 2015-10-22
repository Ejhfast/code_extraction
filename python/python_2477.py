# In google app engine, how to iterate through form fields (python, wsgiref.handlers)
for field in self.request.arguments():
  value = self.request.get(field)
