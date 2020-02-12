#!C:/Users/Tarang/AppData/Local/Programs/Python/Python37-32/python.exe -u

print("Content-Type: text/html")
print()

import cgi,cgitb
cgitb.enable() #for debugging
form = cgi.FieldStorage()
Floor = form.getvalue('Floor')
Room_id = form.getvalue('Room_id')
Room_price  = form.getvalue('Room_price')
Room_type = form.getvalue('Room_type')
Amenities = form.getvalue('Amenities')


import pymysql
db=pymysql.connect("localhost","root","Manchesterutd20","sts")
cursor = db.cursor()
#data=cursor.execute("select max(PCID)+1 from customers")
#print ("your customer ID is :",data)
cursor.execute("INSERT INTO Rooms(Floor,Room_id,Room_price,Room_type,Amenities) VALUES (%s,%s,%s,%s,%s)",(Floor,Room_id,Room_price,Room_type,Amenities))
db.commit()
cursor = db.cursor()

# Execute SQL select statement
sql_query="SELECT DISTINCT R.Floor,R.Room_id,R.Room_price,R.Room_type,R.Amenities FROM Rooms R WHERE TRUE"
cursor.execute(sql_query)

# Get the number of rows in the resultset
data = cursor.fetchall()
attribute_names = [i[0] for i in cursor.description]

print("<style>table { font-family: arial, sans-serif; border-collapse: collapse; width: 100%; } td, th { border: 1px solid #dddddd; text-align: left; padding: 8px; } tr:nth-child(even) { background-color: #dddddd; } </style>")
print("<table><tr>")

for columns in attribute_names:
    print("<th>",columns,"</th>")
print ("</tr>")

for rows in data:
    print ("<tr>");
    for subrows in rows:
        print("<td>",subrows,"</td>")
    print ("</tr>")
print("</table>")