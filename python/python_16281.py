# web.py loads the page even when the class is renamed
if __name__ == "__main__": web.run(urls, globals(), web.reloader)
