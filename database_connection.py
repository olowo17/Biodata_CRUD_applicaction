import pyodbc

DB_NAME="Training"
TABLE_NAME="student_information"


connection = pyodbc.connect(f"DRIVER=ODBC Driver 17 for SQL Server;SERVER=ISW-221130-1108\SQLEXPRESS;DATABASE={DB_NAME};Trusted_Connection=yes;")

cursor=connection.cursor()