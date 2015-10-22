# python web server and periodic tasks
my_task_runner = Monitor(cherrypy.engine, my_task, frequency=3)
my_task_runner.subscribe()
