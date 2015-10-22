# ArcGIS / Python "select by attribute" LIKE
arcpy.SelectLayerByAttribute_management("AllPOSTCODES","NEW_SELECTION",' "PCD" LIKE ' + " 'BT%' ")
