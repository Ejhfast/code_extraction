# django datetime.datetime error
def was_published_today(self):
    return (self.pub_date.date() == datetime.date.today())
