# Is there a way to generate pdf containing non-ascii symbols with pisa from django template?
pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("UTF-8")), result, encoding='UTF-8')
