# python list sequential numbers
&gt;&gt;&gt; mylist = [1,2,3,2,3,5,6,3,7,8,6]
&gt;&gt;&gt; [i+1 for i in range(len(mylist)-1) if mylist[i]&gt;mylist[i+1]]
[3, 7, 10]
