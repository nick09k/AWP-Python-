#!C:\Users\NIKHIL\AppData\Local\Programs\Python\Python38-32\python.exe
import csv,cgi,cgitb
cgitb.enable()
form = cgi.FieldStorage()
uname = form.getvalue('uname')
pswd = form.getvalue('pswd')
flag = 0
file = open(r"D:\python\user_details.csv", 'r')
csv_reader = csv.reader(file)
print("Content-type:text/html\r\n\r\n")
for row in csv_reader:

   if row[0] == uname and row[1] == pswd:
      flag = 1
      break
   else:
     flag = 0

print("<html>")
print("<head>")
print("<title>DASHBOARD</title>")
print("</head>")
print("<body>")
if flag == 1:
   print("<p>You are now logged in!</p")
else:
   print("<p>Incorrect credentials</p>")
print("</body>")

file.close()