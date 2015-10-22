# Python Beautiful Soup 'ascii' codec can't encode character u'\xa5'
page_text = r.text.encode('utf-8').decode('ascii', 'ignore')
page_soupy = BeautifulSoup.BeautifulSoup(page_text)
