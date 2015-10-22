# Is there a best-practice for looping "all the way through" an array in C++?
for (int i=3; i&lt;(3 + size_of_array); ++i)
    std::cout &lt;&lt; a[i % size_of_array] &lt;&lt; '\n';
