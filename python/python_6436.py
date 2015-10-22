# Send Email to multiple recipients from .txt file with Python smtplib
urlFile = open("mailList.txt", "r+")
mailList = [i.strip() for i in urlFile.readlines()]
