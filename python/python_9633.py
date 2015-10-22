# Python/Plone: Getting all unique keywords (Subject)
catalog = self.context.portal_catalog
my_keys = catalog.uniqueValuesFor('Subject')
