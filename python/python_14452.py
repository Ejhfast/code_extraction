# Where is wrong in my SQLite expression?
cursor.execute("INSERT INTO pattent VALUES (?, ?, ?, ?, ?, ?)",
    (PattentNumber, PattentName, PattentInventors, PattentCompany, PattentFiledtime, PattentAbstract))
