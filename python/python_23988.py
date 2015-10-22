# how to cast a variable in xpath python
variabelen = [var1,var2,var3]
for var in variabelen:
    aandeel = tree.xpath('//a[@title="%s"]/text()' % var)
