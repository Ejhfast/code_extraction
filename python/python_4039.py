# Mechanize submit
for each in form.controls[:]:
  if each not "some criteria":
    form.controls.remove(each)
