SELECT SUM(product)
FROM (
  SELECT a.row_num, b.col_num, a.value * b.value as product
  FROM a, b
  WHERE a.col_num = b.row_num
)
WHERE (row_num = 2 AND col_num = 3)
GROUP BY col_num, row_num;