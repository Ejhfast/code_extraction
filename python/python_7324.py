# python issues with MySQL in eclipse
records = cursor.fatchone()
--&gt; should be
records = cursor.fetchone()
