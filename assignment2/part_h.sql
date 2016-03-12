SELECT SUM(A.count * B.count)
FROM
(
   SELECT docid, term, count
   FROM frequency
   WHERE docid = '10080_txt_crude'
) A,
(
   SELECT docid, term, count
   FROM frequency
   WHERE docid = '17035_txt_earn'
) B
WHERE A.term = B.term
ORDER BY A.docid, B.term;