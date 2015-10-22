# Check if a queue is empty in Google App Engine
statsList = taskqueue.QueueStatistics.fetch([taskqueue.Queue("foo"), taskqueue.Queue("bar")])
