-- lists the number of records with the same score in the table second_table of the database hbtn_0c_0
-- the number of records for this score with the label number

select score, count(*) AS number FROM second_table
GROUP BY score
ORDER BY number DESC;
