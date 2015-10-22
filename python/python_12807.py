# Accessing response soap header using suds
print client.last_received().getChild("soap:Envelope").getChild("soap:Header")
.getChild("ResponseHeader").getChild("resultCode").getText()
