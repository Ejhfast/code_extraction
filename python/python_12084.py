# Is there a way to concatenate two arrays in c++ and return them?
vector&lt;int&gt; x = ...;
vector&lt;int&gt; y = ...;
x.insert(x.end(), y.begin(), y.end()); // append y to x
