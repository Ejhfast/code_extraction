# Django natural keys, combination of two values?
def natural_key(self):
    return (self.team.natural_key(),self.year)
