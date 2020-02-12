#!C:/Users/Tarang/AppData/Local/Programs/Python/Python37-32/python.exe -u

print("Content-Type: text/html")
print()

import cgi,cgitb
cgitb.enable() #for debugging
form = cgi.FieldStorage()
Event_type = form.getvalue('Event_type')
Event_name = form.getvalue('Event_name')
No_of_part  = form.getvalue('No_of_part')
Event_id = form.getvalue('Event_id')
Cust_id = form.getvalue('Cust_id')
Room_id = form.getvalue('Room_id')


import pymysql
db=pymysql.connect("localhost","root","Manchesterutd20","sts")
cursor = db.cursor()
#data=cursor.execute("select max(PCID)+1 from customers")
#print ("your customer ID is :",data)
cursor.execute("INSERT INTO Events(Event_type,Event_name,No_of_part,Event_id,Cust_id,Room_id) VALUES (%s,%s,%s,%s,%s,%s)",(Event_type,Event_name,No_of_part,Event_id,Cust_id,Room_id))
db.commit()
cursor = db.cursor()

# Execute SQL select statement
sql_query="SELECT DISTINCT E.Event_type,E.Event_name,E.No_of_part,E.Event_id,E.Cust_id,E.Room_id FROM Events E WHERE TRUE"
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