# XMPPPY have function to manage invitation in client side?
def Authorize(self,jid):
  """ Authorise JID 'jid'. Works only if these JID requested auth previously. """
  self._owner.send(Presence(jid,'subscribed'))
