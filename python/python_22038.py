# Pandas ValueError when attempting to select data using a boolean operator
sve2_all[(sve2_all[' Q l/s'].notnull()) &amp; (sve2_all['Flow_mm/day'].notnull())]
