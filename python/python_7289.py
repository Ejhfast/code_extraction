# Can dynamic backends be started dynamically in Google App Engine?
taskqueue.add(url='/path/to/my/worker/', params={'key': key},
              target='1.backend1')
