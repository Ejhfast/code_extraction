# Regular expressions in SQLalchemy queries?
session.query(Object).filter(Object.column.op('regexp')(REGEX))
