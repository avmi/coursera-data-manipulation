SELECT COUNT(*)
FROM
(
  SELECT DISTINCT docid
  FROM frequency
  WHERE term = 'law' OR term = 'legal'
);