# Updating a sqlite3 Database with QSqlQuery
query.prepare(QString("UPDATE news SET Raw = :value WHERE id = :id "));
query.bindValue(":value", raw);
query.bindValue(":id", news_id);
