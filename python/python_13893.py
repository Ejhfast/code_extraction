# Parsing nginx log data with whitespace as delimiter
ip, date, method, path, status, _ = line.split('\t')
