# Get referenced Model by field name on Django?
statue_a = Statue()
statue_a._meta.get_field('ref_id').rel.to
