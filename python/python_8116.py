# How can I set salt for bcrypt.hashpw?
salt = bcrypt.gensalt()
password = bcrypt.hashpw(password, salt)
repeatpassword = bcrypt.hashpw(repeatpassword,salt)
