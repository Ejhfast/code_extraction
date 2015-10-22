# Return the list of points inside a rectangle
SELECT point.lat, point.long FROM point where rect1.lat &lt;= point.lat and point.lat &lt;= rect2.lat and rect1.long &lt;= point.long and point.long &lt;= rect2.long
