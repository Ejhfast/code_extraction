# Delete intersection between two lists
names_to_remove = set([r.rel.through._meta.object_name for r in m2m_links if not r.rel.through._meta.auto_created])
filtered_list = [r for r in o2m_links if r.rel.through._meta.object_name in names_to_remove]
