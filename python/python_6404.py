# Python, pass a variable by name to a Thread
threading.Thread(target=self._thread_function, args=(arg1,),
                 kwargs={'arg2':arg2}, name='thread_function').start()
