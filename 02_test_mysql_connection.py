from mysql_connection import connection

if connection.is_connected():
    print("Successfully connected to MySQL!")

connection.close()