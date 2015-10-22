# python smtp TypeError: sendmail() missing 1 required positional argument: 'msg'
smtp = smtplib.SMTP("localhost",25)
smtp.sendmail(from_entry.get(),to_entry.get(),msg_entry.get())
