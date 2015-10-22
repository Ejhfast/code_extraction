# How can I determine if one PGArray is included in another using SQLAlchemy sessions?
print sql.literal_column('ARRAY[2]').op('&lt;@')(table.c.lineage)
# ARRAY[2] &lt;@ "treeItems".lineage
