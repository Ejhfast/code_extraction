# Find negative and positive values in numpy array
negavg = numpy.mean(windspeed[windspeed &lt; 0.0])
 posavg = numpy.mean(windspeed[windspeed &gt; 0.0])
