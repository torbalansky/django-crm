#Install mysql
#pip install mysql
#pip install mysql-connector
#pip install mysql-connector-python

import mysql.connector
from decouple import config

db_password = config('DB_PASSWORD')

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd=db_password

    )

#Prepare cursor object
cursorObject = dataBase.cursor()

#Create database
cursorObject.execute("CREATE DATABASE patso1")

print("all good.")