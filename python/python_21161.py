# Handling escapes in pyparsing
Escape = Suppress(Literal("\\")) + Word("\\)]:", exact=1)
Text   = Combine(ZeroOrMore(Escape ^ Regex("[^\\]\\\\:]")))
