SELECT COUNT(*)
FROM
(
  SELECT docid
  FROM frequency
  GROUP BY docid
  HAVING COUNT(term) > 300
);