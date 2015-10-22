# Getting Syntax Error where none was before
connector.execute('''update DATAGERMANY set title_abbreviation_langid=? , title_reliability_langid=? where id_db == ? ''',(lan[-2], lan[-1])) # added paren here
