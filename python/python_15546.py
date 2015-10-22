# Escaped Strings in Parsing Expression Grammars
string         = doubleString / singleString
doubleString   = ~'"([^"]|(\"))*"'
singleString   = ~"'([^']|(\'))*'"
