# Why LIKE without wildcards does not work
SELECT * FROM papers WHERE topic_simple LIKE '% monitor %'
