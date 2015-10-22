# How to pickle numpy's Inf objects?
&gt;&gt;&gt; cPickle.dump(Inf, file("c:/temp/a.pcl",'wb'), -1)
&gt;&gt;&gt; cPickle.load(file("c:/temp/a.pcl",'rb'))
1.#INF                   -- may be platform dependent what prints here.
