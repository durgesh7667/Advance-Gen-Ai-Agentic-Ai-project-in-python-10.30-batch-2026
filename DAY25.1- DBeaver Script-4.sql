SELECT * FROM dataset_1;

SELECT weather,temperature FROM dataset_1 

SELECT * FROM  dataset_1 limit 10

SELECT DISTINCT passanger FROM dataset_1 

select * from dataset_1 where destination='Home'

select * from dataset_1 order by coupon

SELECT destination as Destination FROM dataset_1 

SELECT occupation FROM dataset_1 GROUP BY occupation 

SELECT weather ,AVG(temperature) as avg_temp FROM dataset_1 GROUP BY weather 

SELECT weather ,SUM(temperature) AS sum_temp FROM dataset_1 GROUP BY weather 

SELECT occupation FROM dataset_1 WHERE occupation IN('Sales & Related','Management') 

SELECT DISTINCT temperature FROM dataset_1 WHERE temperature BETWEEN 29 AND 75 

SELECT * FROM dataset_1 WHERE weather LIKE 'Sun%' 

SELECT destination ,passanger FROM(SELECT*FROM dataset_1 WHERE passanger = 'Alone') 

SELECT a.destination,a.time,b.part_of_day FROM dataset_1 a INNER JOIN table_to_join b ON  
a.time=b.time 
 
SELECT DISTINCT destination FROM(SELECT * FROM dataset_1 UNION SELECT * FROM table_to_union) 
