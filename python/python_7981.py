# list comprehension equivalent without producing a throwaway list
&gt;&gt;&gt; consume(some_func(x) for x in some_list if x&gt;5)
