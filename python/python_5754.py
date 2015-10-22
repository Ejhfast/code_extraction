# How to convert 32digit long info hash to 40 digit long info hash in python?
import base64
base64.b16encode(base64.b32decode("&lt;your hash goes here&gt;"))
