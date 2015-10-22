# How do I do a jointplot in R the same way as I do it python (seaborn package)
devtools::install_github("WinVector/WVPlots")
library(WVPlots)
ScatterHist(diamonds, "price", "carat")
