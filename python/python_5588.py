# Saving text file contents to DB: "Incorrect string value: '\xEF\xBB\xBF# W...' for column 'contents' at row 1"
alter table yourTableName DEFAULT CHARACTER SET utf8;
