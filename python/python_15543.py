# exclude findAll result set
css_files = soup.findAll('link',{'rel':'stylesheet', 'media': lambda L: L != 'print'})
# [&lt;link href="/assets/application-b275a30a2c6726e3fabb10517f7cb812.css" media="all" rel="stylesheet" type="text/css"/&gt;]
