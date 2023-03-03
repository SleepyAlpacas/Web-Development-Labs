#!/usr/bin/perl -wT

use CGI':standard'; 
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use File::Basename;
$CGI::POST_MAX = 1024 * 2000;
use strict;
print "Content-type: text/html\n\n";



my $firstName = param( 'firstName' );
my $lastName = param ( 'lastName' );
my $street = param ( 'street' );
my $city = param ( 'city' );
my $postalCode = param ( 'postalCode' );
my $province = param( 'province' );
my $phone = param( 'phone' );
my $email = param( 'email' );
my $photo = param( 'photo' );

my $upload_dir = "../temp";
my $safe_filename_characters = "a-zA-Z0-9_.-";
my $query = new CGI;
my $filename = $query->param( 'photo' );
my ( $name, $path, $extension ) = fileparse ( $filename, '\..*' ); 
$filename = $name . $extension;
$filename =~ tr/ /_/; $filename =~ s/[^$safe_filename_characters]//g;

if ( $filename =~ /^([$safe_filename_characters]+)$/ ) {
	$filename = $1;
} 
else {
	die "Filename contains invalid characters"; 
}

my $upload_filehandle = $query->upload("photo");
open ( UPLOADFILE, ">$upload_dir/$filename" ) or die "$!"; 
binmode UPLOADFILE; while ( <$upload_filehandle> ) { print UPLOADFILE; } close UPLOADFILE;

print "<div style='border:5px solid black;text-align:center;background-color:PowderBlue;'>";

if ($firstName){
	print "<p style='color:green'>First Name: $firstName</p>";
}
else{
	print "<p style='color:red'>INVALID FIRST NAME: $firstName</p>";
}

if ($lastName){
	print "<p style='color:green'>Last Name: $lastName</p>";
}
else{
	print "<p style='color:red'>INVALID LAST NAME: $lastName</p>";
}

if ($street){
	print "<p style='color:green'>Address: $street\n</p>";
}
else{
	print "<p style='color:red'>INVALID ADDRESS: $street</p>";
}

if ($city){
	print "<p style='color:green'>City: $city\n</p>";
}
else{
	print "<p style='color:red'>INVALID CITY: $city</p>";
}


if ($postalCode =~ m/(\D)(\d)(\D) (\d)(\D)(\d)/){
	print "<p style='color:green'> Postal Code: $postalCode";
}
else{
	print "<p style='color:red'>INVALID POSTAL CODE: $postalCode</p>";
}

if ($province){
	print "<p style='color:green'>Province: $province\n</p>";
}

if ($phone =~ m/^\d{10}$/){
	print "<p style='color:green'>Phone Number: $phone </p>";
}
else{
	print "<p style='color:red'>INVALID PHONE: $phone</p>";
}

if ($email =~ m/^\w+@\w+\.\w+$/){
	print "<p style='color:green'>Email: $email </p>";
}
else{
	print "<p style='color:red'>INVALID EMAIL: $email</p>";
}

print "</div>";

if ($filename){
	print "<img src=../temp/$filename>	";
}