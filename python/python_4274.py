# Dynamically add ManyToMany relationship to Django objects
company, was_created = Company.objects.get_or_create(name=info)
                        setattr(self,key, [company,])
