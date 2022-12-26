-- Query to display the top 3 cities temp during July and August
SELECT city, AVG(value) as avg_temp 
FROm temperatures
WHERE month=7 OR month=8 
GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
