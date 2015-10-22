# lxml stops when it encounters a missing tag
titlex = info.find('.//xmlns:Title', namespaces=nsmap)
  title = titlex.text if titlex != None else ''
