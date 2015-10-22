# Django - Keeping the original method's work and add new custom validation
def clean(self):
    super(MyUserAdminForm, self).clean()
    # more cleaning
