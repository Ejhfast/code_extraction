# ArcMap 10.2: Custom ArcGIS tool.
result = arcpy.GetCount_management(output_features)
count = int(result.getOutput(0))
arcpy.AddWarning("There are {0} in the new feature class.".format(count))
