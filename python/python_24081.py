# merging two tables by placing data when condition satisfies
SELECT B.NO, B.v1 AS V1, A.a2 AS V2
 FROM A INNER JOIN B
 WHERE A.a1 = B.v1;
