--  script that lists all records of the table second_table of the database hbtn_0c_
-- Don’t list rows without a name value
-- Results should display the score and the name (in this order)
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC;
