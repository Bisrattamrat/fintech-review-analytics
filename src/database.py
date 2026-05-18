import psycopg2

try:
    connection = psycopg2.connect(
        host="localhost",
        database="bank_reviews",
        user="postgres",
        password="your_password"
    )

    print("Database connected successfully.")

except Exception as e:
    print(f"Database connection failed: {e}")