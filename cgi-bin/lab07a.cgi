#!/usr/bin/perl

use CGI':standard'; 
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
print "Content-type: text/html\n\n";
print qq(<head><link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Smokum&display=swap" rel="stylesheet"> </head>);

print qq(<p style="text-align:center; color:orange; font-family: 'Smokum', cursive; font-size: 40px;">This is my Perl program</p>);
