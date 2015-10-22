# Adding columns from joined table
models.Detail.query.join(details_usages).add_columns(details_usages.c.is_required).all()
