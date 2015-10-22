# Parser in dateutil fails to render hour correctly
&gt;&gt;&gt; parser.parse("20130501200439+01'00'".replace("'", ""))
datetime.datetime(2013, 5, 1, 20, 4, 39, tzinfo=tzoffset(None, 3600))
