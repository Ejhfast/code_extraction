# Is it possible to stop sqlite treating double quoted identifiers as strings?
SELECT bar."foo", a."baz" FROM bar, blah AS a
