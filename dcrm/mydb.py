import mysql.connector

dataBase = mysql.connector.connect(host="localhost", user="root", passwd="123")

cursor = dataBase.cursor()

cursor.execute('CREATE DATABASE db1')

