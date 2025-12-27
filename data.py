# python --> database : mysql-python-connector

import mysql.connector

def db_connection():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        database="EmployeeManagementSystem",

    )


print("db connected successfully")
