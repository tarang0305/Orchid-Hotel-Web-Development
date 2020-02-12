#!C:/Users/Tarang/AppData/Local/Programs/Python/Python37-32/python.exe -u
print("Content-Type: text/html")
print()

import cgi,cgitb
cgitb.enable() #for debugging
form = cgi.FieldStorage()
name = form.getvalue('fname')
print("Name of the user is:",name)

import pymysql

db = pymysql.connect("localhost","root","Manchesterutd20","sts" )

cursor =  db.cursor()

cursor.execute(name)

name = cursor.fetchall()

print (name)

db.close()