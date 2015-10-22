# SQLAlchemy: How to get result in a list while querying single columns of table using all()?
&gt;&gt;&gt; units_ability = [(1L,), (2L,)] # units_abilities = (Session....all())
&gt;&gt;&gt; [x for (x,) in units_ability]
[1L, 2L]
