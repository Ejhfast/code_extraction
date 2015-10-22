# In Python, identify parts of an e-mail address
import email.utils
map(email.utils.parseaddr, email_list)
