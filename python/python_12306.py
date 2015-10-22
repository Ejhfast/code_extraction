# Django Tag model design
tags = models.ManyToManyField(Tag,related_name='photos')
