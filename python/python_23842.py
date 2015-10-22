# View Django query in SQL
&gt;&gt;&gt; entries = Catalog.objets.exclude(...)
&gt;&gt;&gt; print entries.query
