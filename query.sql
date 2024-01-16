--Отримати середні тижневі продажі за типом магазину
SELECT s.type, AVG(t.weekly_sales) AS average_weekly_sales
FROM Train t
JOIN stores s ON t.store = s.store
GROUP BY s.type;
--Визначаити кількість магазинів кожного типу
SELECT s.type, COUNT(*) AS store_count
FROM stores s
LEFT JOIN Train t ON s.store = t.store
GROUP BY s.type;
--Знайдіть максимальну температуру за датою
SELECT f.date, AVG(f.temperature) AS average_temperature
FROM features f
LEFT JOIN Train t ON f.store = t.store AND f.date = t.date
GROUP BY f.date;