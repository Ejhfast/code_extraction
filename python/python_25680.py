# Django non persistent model field
self.temp_pw = user.generate_password()
user.set_password(self.temp_pw)
