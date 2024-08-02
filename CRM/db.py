import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'pantheon1823',
)

cursor = database.cursor()


cursor.execute("CREATE DATABASE crm_django")
print('database created')
