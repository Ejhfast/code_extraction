# How to share files using drive-sdk?
drive.permissions().insert(fileId=file['id'], body=Permission, sendNotificationEmails=True ).execute()
