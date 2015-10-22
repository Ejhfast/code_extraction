# Pika worker throws exception when running channel.declare_queue
connection = pika.BlockingConnection(pika.ConnectionParameters(host=cmdargs.server))
