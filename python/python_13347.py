# lxml not properly parsing tags with multiple classes
a.xpath('.//span[contains(concat(" ", @class, " "), " cut ")]')
