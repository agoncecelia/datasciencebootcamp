# Execute these for creating new user and granting privileges on MySQL

#CREATE DATABASE datasciencebootcamp;
#
#CREATE USER 'datasciencebootcamp' identified by 'datasciencebootcamp';
#
#GRANT ALL PRIVILEGES ON datasciencebootcamp . * TO 'datasciencebootcamp';

import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    database="datasciencebootcamp",
    user="datasciencebootcamp",
    password="datasciencebootcamp")

cursor = conn.cursor()

first_name = input("Provide first_name: ")
last_name = input("Provide last_name: ")
email = input("Provide email: ")
sql = "INSERT INTO Users (firstname, lastname, email) VALUES (%s, %s, %s)"
val = (first_name, last_name, email)
cursor.execute(sql, val)
conn.commit()

cursor.close()
