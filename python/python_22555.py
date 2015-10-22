# How to get a nested function's namespace in Python?
&gt;&gt;&gt; [caller.__closure__[0].cell_contents for caller in callers]
[&lt;function random_function_1 at 0x1004e0de8&gt;, &lt;function random_function_2 at 0x1004e0e60&gt;, &lt;function random_function_3 at 0x103b70de8&gt;]
