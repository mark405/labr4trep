import main
import psycopg2
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

db_params = main.db_params
execute_query = main.execute_query
query_2a = main.query_2a
query_2b = main.query_2b
query_2c = main.query_2c

def visualize_query_2a(result):
    types = [row[0] for row in result]
    avg_sales = [row[1] for row in result]

    plt.bar(types, avg_sales)
    plt.xlabel('Store Type')
    plt.ylabel('Average Weekly Sales')
    plt.title('Average Weekly Sales by Store Type')
    plt.show()


def visualize_query_2b(result):
    types = [row[0] for row in result]
    store_count = [row[1] for row in result]

    plt.bar(types, store_count)
    plt.xlabel('Store Type')
    plt.ylabel('Number of Stores')
    plt.title('Number of Stores for Each Store Type')
    plt.show()


def visualize_query_2c(result):
    dates = [row[0] for row in result]
    max_temperature = [row[1] for row in result]

    plt.plot(dates, max_temperature, marker='o')
    plt.xlabel('Date')
    plt.ylabel('Max Temperature')
    plt.title('Max Temperature by Date')
    plt.show()


def main():
    # Connect to PostgreSQL
    try:
        conn = psycopg2.connect(**db_params)
        cursor = conn.cursor()

        # Execute queries
        result_2a = execute_query(query_2a, cursor)
        result_2b = execute_query(query_2b, cursor)
        result_2c = execute_query(query_2c, cursor)

        # Visualize results
        visualize_query_2a(result_2a)
        visualize_query_2b(result_2b)
        visualize_query_2c(result_2c)

    except psycopg2.Error as e:
        print(f"Error: {e}")

    finally:
        # Close the connection
        conn.close()


if __name__ == "__main__":
    main()
