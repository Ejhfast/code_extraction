# scrapy deltafetch configuration not working
def parse_funstuff(self, response):
        filename = response.url.split("/")[-1]
        open(filename, 'wb').write(response.body)
