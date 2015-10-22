# Twisted redirect subdirectory to another domain
from twisted.web.util import Redirect
fooDotComResource.putChild("bar", Redirect("http://foobar.com/bar"))
