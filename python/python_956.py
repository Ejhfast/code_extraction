# Getting text values from XML in Python
dom = parseString('&lt;something&gt;&lt;data&gt;I WANT THIS&lt;/data&gt;&lt;/something&gt;')
data = dom.getElementsByTagName('data')[0].childNodes[0].data
