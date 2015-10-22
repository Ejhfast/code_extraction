# python: Given a BytesIO buffer, generate img tag in html?
import base64
img_tag = "&lt;img src='data:image/png;base64," + base64.b64encode(img_buffer.getvalue()) + "'/&gt;"
