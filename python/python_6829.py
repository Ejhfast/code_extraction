# xpath not operator and multiple select
queryStr = "//a[contains(@href,'/women-') and not(contains(@href,'/women-shoes'))]"
for link in hxs.select(queryStr):
    self.log("LINKS2 :: %s" % attribute::href())
