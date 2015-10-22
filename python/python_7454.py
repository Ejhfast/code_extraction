# python, how i do xml = '<start>%??</start>' % datetime.datetime
mydate = datetime.datetime.now()
myxmldate = '&lt;start&gt;%s&lt;/start&gt;' % mydate.isoformat()
