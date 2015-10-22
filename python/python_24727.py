# celery: remove empty queues that are more than 5 minutes old?
sudo rabbitmqctl set_policy expiry ".*" '{"expires":300000}' --apply-to queues
