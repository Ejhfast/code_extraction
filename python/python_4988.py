# Gql get all children of ancestor without the ancestor itself
SELECT * FROM Post WHERE ANCESTOR IS :1 AND __key__ &lt; :2
SELECT * FROM Post WHERE ANCESTOR IS :1 AND __key__ &gt; :2
