# Creating a get_absolute_url()
def get_absolute_url(self):
    return "/event/%d" % self.id
