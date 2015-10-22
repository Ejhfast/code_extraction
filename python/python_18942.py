# How to post a task on a celery-rabbitmq queue in PHP?
$exchange = 'demo';
$binding = 'demo';
$c = new Celery('localhost', 'guest', 'guest', '/', $exchange, $binding);
