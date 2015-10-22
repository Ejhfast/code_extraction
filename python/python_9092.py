# How do I automate Google App Engine upload_data with --passin and subprocess.Popen?
file = open("upload.pass")
process = subprocess.Popen([..., "--passin"], stdin=file)
process.wait()
