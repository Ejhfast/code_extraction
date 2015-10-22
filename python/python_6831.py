# Get initial data of form fields
for field in SettingsForm().fields:
    print field.initial
