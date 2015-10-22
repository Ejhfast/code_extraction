# Algorithm to determine the closest date to some date input
SELECT MAX(Date)
FROM MyDates
WHERE Date &lt;= InputDate;
