# Beginner - Python 2.7.2, ArcGIS 10.1 Multiple 'or' conditions, same action
for lyr in arcpy.mapping.ListLayers(mxd, "", df):
    if lyr.name() in ['name1', 'name2', 'name3']:
        arcpy.mapping.RemoveLayout(df, lyr)
