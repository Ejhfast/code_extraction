# How can I save a file that is 1 row N number of data points, as a file that is 1 column N number of data points?
file("mockdata.txt", "r").read().replace(",", "\n")
