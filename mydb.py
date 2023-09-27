#Install mysql
#pip install mysql
#pip install mysql-connector
#pip install mysql-connector-python

import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Gengen90!'

    )

#Preprae cursor object
cursorObject = dataBase.cursor()

#Create database
cursorObject.execute("CREATE DATABASE patso1")

print("all good.")