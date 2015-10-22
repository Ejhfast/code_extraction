# Unable to upload a file to Google Drive
this_file = drive.CreateFile()
this_file.SetContentFile('apple.txt') # Read file and set it as a content of this instance.
this_file.Upload() # Upload it
