# adding task to non-default queue in google app engine
q = taskqueue.Queue('slowQueue')
task = taskqueue.Task(url='/worker/slow', params={'name': name})
q.add(task)
