# Python regex to match string
def splitAppId(self, url):
        idMatch = re.search(r'/id([^/]+)\?[^/]*$', url)
        return idMatch.group(1)
