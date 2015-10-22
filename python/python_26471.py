# Dropbox API Shared Folders
url, params, headers = client.request("/shared_folders/", {}, method='GET')
response = client.rest_client.GET(url, headers)
