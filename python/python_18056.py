# How could I search a tag that contain <sup> in a Python beautifulsoup find() call
soup.find(lambda tag: tag.name == 'b' and
          "Particulate Matter" in tag.text)
