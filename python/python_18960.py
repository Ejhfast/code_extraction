# Class Inheritance, How to add fields to a variable already set in a parent class
class ProfileCreateForm(Turtle_BaseInfoForm):
    fields = Turtle_BaseInfoForm.fields + ('bio',)
