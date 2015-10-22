# Python sort lists with lists inside
&gt;&gt;&gt; lists=[[3,2,1,4],["three","two","one","four"],["tres","dos","uno","cuatro"]]
&gt;&gt;&gt; [[x for i, x in sorted(zip(lists[0], sublist))] for sublist in lists]
[[1, 2, 3, 4], ['one', 'two', 'three', 'four'], ['uno', 'dos', 'tres', 'cuatro']]
