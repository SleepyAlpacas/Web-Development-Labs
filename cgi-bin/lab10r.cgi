#!/usr/bin/ruby
puts "Content-type: text/html\n\n"
require 'cgi'
cgi = CGI.new
puts "<html> <body style='margin:0'>"
puts "<h1 style='text-align:center; background-color:orange; color:lime; font-size: 60px'>" + cgi['city'].capitalize() + ", "+ cgi['province'].capitalize() + ", " + cgi['country'].capitalize() + "</h1>"
puts "<p style='text-align:center;'> ruby page btw </p>"
puts "<img style='width:100%;' src='" + cgi['url'] + "'>"
puts "</body></html>"


