# How can I detect Heroku's environment?
on_heroku = false
if 'YOUR_ENV_VAR' in os.environ:
  on_heroku = true
