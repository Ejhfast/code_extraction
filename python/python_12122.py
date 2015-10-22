# Open source project for downloading mailing list archives preferably in Python
import mailbox
mails = mailbox.mbox(filename.mbox)
for message in mails: print message['subject']
