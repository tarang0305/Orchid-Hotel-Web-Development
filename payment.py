#!C:/Users/Tarang/AppData/Local/Programs/Python/Python37-32/python.exe -u

print("Content-Type: text/html")
print()

import cgi,cgitb
cgitb.enable() #for debugging
form = cgi.FieldStorage()
Pay_type = form.getvalue('Pay_type')
Cust_id = form.getvalue('Cust_id')
Pay_amount  = form.getvalue('Pay_amount')
Pay_id = form.getvalue('Pay_id')
Pay_date = form.getvalue('Pay_date')
Book_id = form.getvalue('Book_id')

import pymysql
db=pymysql.connect("localhost","root","Manchesterutd20","sts")
cursor = db.cursor()
#data=cursor.execute("select max(PCID)+1 from customers")
#print ("your customer ID is :",data)
cursor.execute("INSERT INTO Payment(Pay_type,Cust_id,Pay_amount,Pay_id,Pay_date,Book_id) VALUES (%s,%s,%s,%s,%s,%s)",(Pay_type,Cust_id,Pay_amount,Pay_id,Pay_date,Book_id))
db.commit()
cursor = db.cursor()

# Execute SQL select statement
sql_query="SELECT DISTINCT P.Pay_type,P.Cust_id,P.Pay_amount,P.Pay_id,P.Pay_date,P.Book_id FROM Payment P WHERE TRUE"
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