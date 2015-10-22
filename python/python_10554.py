# How do I prevent a list comprehension from including empty values?
columns1 = [row[d] for d in cols if row[d] != '']
                                    ^^^^ ^
