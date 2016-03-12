SELECT MAX(count)
FROM
(
  SELECT SUM(A.count * B.count) count
  FROM
  (
     SELECT 'q' AS docid, 'washington' AS term, 1 AS count

     UNION

     SELECT 'q' AS docid, 'taxes' AS term, 1 AS count

     UNION

     SELECT 'q' AS docid, 'treasury' as term, 1 AS count
  ) A,
  (
     SELECT * FROM frequency
  ) B
  WHERE A.term = B.term
  GROUP BY B.docid
);