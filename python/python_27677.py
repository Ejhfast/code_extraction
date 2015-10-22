# Need help on tornado coroutines
if __name__ == "__main__":
    from tornado.ioloop import IOLoop
    print IOLoop.instance().run_sync(routine1)
