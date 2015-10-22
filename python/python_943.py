# Parse custom URIs with urlparse (Python)
parts = urlparse.urlparse("qqqq://base/id#hint")
fake_url = "http:" + parts[2]
parts2 = urlparse.urlparse(fake_url)
