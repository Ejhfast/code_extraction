# Python equivalent to Java's Class.getResource
import pkg_resources
my_data = pkg_resources.resource_string(__name__, "foo.dat")
