# Create formatted values in Dictionary python
return {g:tuple(s for s in self.db[g]) for g in self.db}
