# change the date format in a csv file
library(lubridate)
YourData$date &lt;- dmy(YourData$date)
YourData$date &lt;- format(YourData$date, format = "%Y-%m-%d")
