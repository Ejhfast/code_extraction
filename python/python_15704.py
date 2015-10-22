# Selecting Node with specific text that have a quote in them
node = self.productDoc.xpath("/product[name/value[text() = \"{0}\"]]".format(self.Title))
