# How do I use bugzilla's webservice xml-rpc with python?
bz = bugzilla.Bugzilla(url='https://bugzilla.redhat.com/xmlrpc.cgi')
bug = bz.getbug(495561)
