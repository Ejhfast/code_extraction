# django foreignkey - format output value in selectlist
def user_new_unicode(self):
    return self.get_full_name()
User.__unicode__ = user_new_unicode #or User.__str__ = user_new_unicode
