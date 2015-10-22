# Running python app on localhost
if __name__ == '__main__' :
  app = web.application(urls, globals())
  app.run()
