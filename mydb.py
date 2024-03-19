
import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'E@rnesty13579wj'
)

# prepare a cursor object
curserObject = dataBase.cursor()

# create database
curserObject.execute("CREATE DATABASE asonjaco")

print("All Done!")
