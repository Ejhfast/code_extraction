# XML to pandas dataframe
DataFrame.from_records([(int(word['x1']), int(word['x2']))
                        for word in soup.page.findAll('word')],
                       columns=('x1', 'x2'))
