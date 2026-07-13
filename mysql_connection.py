import mysql.connector

def get_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="myntra_user",
        password="Your_Password",
        database="ab_testing_platform"
    )
    return connection