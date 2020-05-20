#!C:\Users\NIKHIL\AppData\Local\Programs\Python\Python38-32\python.exe

import cgi,cgitb
cgitb.enable()

form = cgi.FieldStorage()
area_text = form.getvalue('text_feild')
x = len(area_text)
reversed_text = area_text[x::-1]

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>REVERSED MESSAGE</title>")
print("</head>")
print("<body>")
print("<h3>  Text field Details are reversed : </h3>")
print("<p>%s</p>" % (reversed_text))
print("</body>")
print("</html>")