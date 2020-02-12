#!C:/Users/Tarang/AppData/Local/Programs/Python/Python37-32/python.exe -u

print("Content-Type: text/html")
print()

import cgi,cgitb
cgitb.enable() #for debugging
form = cgi.FieldStorage()
Cust_id = form.getvalue('Cust_id')
Cust_name = form.getvalue('Cust_name')
Cust_type = form.getvalue('Cust_type')
Cust_ph = form.getvalue('Cust_ph')
Cust_age = form.getvalue('Cust_age')
Cust_pref = form.getvalue('Cust_pref')


import pymysql
db=pymysql.connect("localhost","root","Manchesterutd20","sts")
cursor = db.cursor()
#data=cursor.execute("select max(PCID)+1 from customers")
#print ("your customer ID is :",data)
cursor.execute("INSERT INTO Customer(Cust_id,Cust_name,Cust_type,Cust_ph,Cust_age,Cust_pref) VALUES (%s,%s,%s,%s,%s,%s)",(Cust_id,Cust_name,Cust_type,Cust_ph,Cust_age,Cust_pref))
db.commit()
cursor = db.cursor()

# Execute SQL select statement
sql_query="SELECT DISTINCT C.Cust_id,C.Cust_name,C.Cust_type,C.Cust_ph,C.Cust_age,C.Cust_pref FROM Customer C WHERE TRUE"
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