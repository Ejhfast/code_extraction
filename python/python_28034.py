# Create a folder (if not exists) on google drive and upload a file to it using Python script
file1 = drive.CreateFile({'title': fname,
    "parents":  [{"id": id}],
    "mimeType": "application/vnd.google-apps.folder"})
