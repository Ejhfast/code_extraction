# Python rearrange list starting from a certain element
&gt;&gt;&gt; original_list, my_index = [1, 2, 3, 4, 5], 2
&gt;&gt;&gt; original_list[my_index + 1:] + original_list[:my_index + 1]
[4, 5, 1, 2, 3]
