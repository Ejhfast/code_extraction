# There is an example of Spyne client?
c = ZeroMQClient("tcp://127.0.0.1:5001", radiante_rpc)
print c.service.whoiam()
