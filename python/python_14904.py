# split array to sub array by step in Ruby
a = [1,2,3,4,5,6,7,8,9]
a.values_at(*(1...7).step(2))
#=&gt; [2, 4, 6]
