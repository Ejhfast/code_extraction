# adding to StringListProperty
tags = self.request.get('tags').split(',')
img_ref.tags.extend(tags)
img_ref.put()
