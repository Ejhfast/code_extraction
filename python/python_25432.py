# What is the Java equivalent to Python's reduce function?
List&lt;Integer&gt; numbers = Arrays.asList(new Integer[] { 1, 2, 3, 4, 5 });
Optional&lt;Integer&gt; sum = numbers.stream().reduce((a, b) -&gt; a + b);
System.out.println(sum.get());
