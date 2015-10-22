# Django Admin foreign key
def get_status_name(self):
    a = self.followup_set.latest('follow_up_date')
    return a.status.status_name
