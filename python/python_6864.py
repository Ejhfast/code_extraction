# Python threading: What am I missing? (task_done() called too many times)
q.put(QueuedCall('twitter', q, Twitter.get_status, [5,], __op_complete))
