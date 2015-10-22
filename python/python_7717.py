# Google Apps Engine reading URL Query (python)
def get(self):
  city = self.request.get('city')
  state = self.request.get('state')
