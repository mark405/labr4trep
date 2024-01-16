INSERT INTO stores (store, type, size) VALUES
   (1, 'Grocery', 5000),
   (2, 'Electronics', 3000),
   (3, 'Clothing', 2000);
INSERT INTO features (store, date, temperature, fuel_price, cpi) VALUES
     (1, '2024-01-15', 25.5, 2.8, 150.5),
     (2, '2024-01-16', 22.0, 3.2, 155.2),
     (3, '2024-01-17', 18.5, 2.5, 145.8);
INSERT INTO Train (store, dept, date, weekly_sales, is_holiday) VALUES
    (1, 101, '2024-01-15', 50000.0, false),
    (2, 201, '2024-01-16', 75000.0, true),
    (3, 301, '2024-01-17', 60000.0, false);