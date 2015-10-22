# pymongo replication secondary readreference not work
&gt;&gt;&gt; db = ReplicaSetConnection("morton.local:27017", replicaSet='foo').test
&gt;&gt;&gt; from pymongo import ReadPreference
&gt;&gt;&gt; db.read_preference = ReadPreference.SECONDARY
