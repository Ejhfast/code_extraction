# Specific Quote Issue
def save(self):
    today = datetime.date.today()
    self.quote = "%s-%s" % (str(today.year)[2:4], self.quote)
