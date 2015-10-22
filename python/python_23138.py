# Capturing filename with python requests toolbelt
files = MultipartEncoder(fields={'file': (file, open(file, "rb"), 'audio/mpeg')})
audio_headers = {'Authorization': 'Bearer ' + token, 'Content-Type': files.content_type}
add_file = requests.post(file_url, headers=audio_headers, data=files)
