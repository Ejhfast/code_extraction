# Python Google App Engine query inside transaction without ancestor?
page = Page.all().ancestor(person).filter("url =",page.url).get()
