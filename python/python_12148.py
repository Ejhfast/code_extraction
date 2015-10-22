# Accessing files in python egg from inside the egg
from pkg_resources import resource_stream, Requirement
resource_stream(Requirement.parse("restez==0.3.2"), "restez/httpconn.py")
