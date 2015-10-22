# Regex recurses too often
good:(?P&lt;quote&gt;["'`])?(?P&lt;value&gt;(?(quote)((?!(?P=quote)).|((?=(?P=quote)).){2})*|[^;\s]*))(?(quote)(?P=quote)|)
bad :(?P&lt;quote&gt;["'`])?(?P&lt;value&gt;(?(quote)((?!(?P=quote)).|((?=(?P=quote)).){2})*|[^\s;]*))(?(quote)(?P=quote)|)
