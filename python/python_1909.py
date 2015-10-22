# Where is the full JID value when using xmpppy?
c = xmpp.client.Client(...)
# connect
jid = xmpp.JID(node=c.User, domain=c.Server, resource=c.Resource)
