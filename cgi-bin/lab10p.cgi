#!/usr/bin/python
import cgi, cgitb
print "Content-type:text/html\n\n"

form = cgi.FieldStorage()
country = form.getvalue('country')
city = form.getvalue('city')
province = form.getvalue('province')
url = form.getvalue('url')
print "<html> <body style='margin:0'>"
print "<h1 style='text-align:center; background-color:orange; color:lime; font-size: 60px'>" + city.upper() + ", "+ province.upper() + ", " + country.upper() + "</h1>"
print "<p style='text-align:center;'> python page btw </p>"
print "<img style='width:80%;border: 40px solid purple; margin: 0 auto; display: block;' src ='" + url + "'>"
print "</body> </html>"