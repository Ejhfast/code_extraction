# Django Admin Custom Form Not Saving
def save(self, *args, **kwargs):
    print("HI")
    return super(Edit_Story_Form, self).save(*args, **kwargs)
