# How can I get the specific database error message from exception DatabaseError?
e.__cause__.__context__.excepinfo[2]
