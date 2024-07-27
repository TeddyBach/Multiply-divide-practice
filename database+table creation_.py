import mysql.connector
from mysql.connector import Error
from config import user, password, host

def check_and_create_database(host, user, password, database_name):
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )
       
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("SHOW DATABASES LIKE %s", (database_name,))
            result = cursor.fetchone()
           
            if result:
                print(f"Database '{database_name}' exists.")
            else:
                print(f"Database '{database_name}' does not exist. Creating it now.")
                cursor.execute(f"CREATE DATABASE {database_name}")
                print(f"Database '{database_name}' created.")
           
            cursor.close()

    except Error as e:
        print(f"Error: {e}")

    finally:
        if connection.is_connected():
            connection.close()
            print("MySQL connection is closed.")

def create_table_if_not_exists(host, user, password, database_name):
    try:
        # Connect to the specific database
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database_name
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Multiply_divide_practice (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    Date_completed DATETIME,
                    Number_correct INT,
                    Total_number INT,
                    Time_spent TIME,
                    Times_table INT,
                    Time_per_question TIME,
                    name TEXT
                )
            """)
            print("Table 'Multiply_divide_practice' ensured to exist.")
            cursor.close()

    except Error as e:
        print(f"Error: {e}")

    finally:
        if connection.is_connected():
            connection.close()
            print("MySQL connection is closed.")

# Configuration
database_name = "Multiply_divide_practice"

# Check and create database if not exists
check_and_create_database(host, user, password, database_name)

# Connect to the database and create the table if not exists
create_table_if_not_exists(host, user, password, database_name)
