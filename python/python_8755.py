# Deal with overflow in exp using numpy
import bigfloat
bigfloat.exp(5000,bigfloat.precision(100))
# -&gt; BigFloat.exact('2.9676283840236670689662968052896e+2171', precision=100)
