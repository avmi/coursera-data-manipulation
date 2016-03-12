SELECT COUNT(*)
FROM
(
  SELECT SUM(docid)
  FROM
  (
    SELECT docid, term
    FROM frequency
    WHERE term = "transactions"

    UNION

    SELECT docid, term
    FROM frequency
    WHERE term = "world"
  )
  GROUP BY docid
  HAVING COUNT(*) = 2
);