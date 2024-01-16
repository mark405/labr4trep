import psycopg2

# Database connection parameters
db_params = {
    'host': 'localhost',
    'port': '5432',
    'database': 'lab4',
    'user': 'postgres',
    'password': 'postgres'
}

# Queries
query_2a = """
SELECT s.type, AVG(t.weekly_sales) AS average_weekly_sales
FROM Train t
JOIN stores s ON t.store = s.store
GROUP BY s.type;
"""

query_2b = """
SELECT s.type, COUNT(*) AS store_count
FROM stores s
LEFT JOIN Train t ON s.store = t.store
GROUP BY s.type;
"""

query_2c = """
SELECT f.date, MAX(f.temperature) AS max_temperature
FROM features f
LEFT JOIN Train t ON f.store = t.store AND f.date = t.date
GROUP BY f.date;
"""

def execute_query(query, cursor):
    cursor.execute(query)
    result = cursor.fetchall()
    return result

def main():
    # Connect to PostgreSQL
    try:
        conn = psycopg2.connect(**db_params)
        cursor = conn.cursor()

        # Execute queries
        result_2a = execute_query(query_2a, cursor)
        result_2b = execute_query(query_2b, cursor)
        result_2c = execute_query(query_2c, cursor)

        # Print results
        print("Result of Query 2a:")
        print(result_2a)

        print("\nResult of Query 2b:")
        print(result_2b)

        print("\nResult of Query 2c:")
        print(result_2c)

    except psycopg2.Error as e:
        print(f"Error: {e}")

    finally:
        # Close the connection
        conn.close()

if __name__ == "__main__":
    main()
