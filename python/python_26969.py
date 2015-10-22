# Reload a csv file and call the same view with it
d3.csv('static/csv/data.csv?_=' + Math.random(), function(data) {
