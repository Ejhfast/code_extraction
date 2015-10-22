# Pika and RabbitMQ - create a queue on a specific node
arguments["x-ha-policy"] = "nodes"
arguments["x-ha-policy-params"] = 'rabbit@node1'
