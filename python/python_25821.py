# Prepopulated fields following 'save as new' Django
def save(self, *args, **kwargs):
        self.slug = self.name
        super(Survey, self).save(*args, **kwargs)
