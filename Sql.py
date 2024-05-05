import mysql.connector
from mysql.connector import Error

try:
    # Replace the next variables with your SQL instance information
    connection = mysql.connector.connect(
        host='34.116.83.30',  # e.g., 35.233.100.20
        database='DDP',
        user='sqlserver',
        password='drRfN_h8*Z[Ihu37'
    )

    if connection.is_connected():
        db_info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
