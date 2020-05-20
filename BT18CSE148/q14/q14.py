
import mysql.connector
  
#Create the connection object
myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "root")
  
#creating the cursor object
cursor_obj = myconn.cursor()
  
try:
    dbs = cursor_obj.execute("Show databases")
except:
    myconn.rollback()
for x in cursor_obj:
    print(x)
myconn.close()
