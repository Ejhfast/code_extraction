# How do you base-64 encode a PNG image for use in a data-uri in a CSS file?
import base64
encoded = base64.b64encode(open("filename.png", "rb").read())
