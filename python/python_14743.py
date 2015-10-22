# Processing image from the blob GAE
from google.appengine.api.images import get_serving_url
url = get_serving_url( "blobkey")
