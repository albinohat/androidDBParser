## File Name: androidDBParser.py
##
## Author(s): Daniel "Albinohat" Mercado
##
## Purpose: This script open and parse through the databases used to store
##          data for Android applications and store them as objects.
##
## TODO - 
##
## Standard imports (Static)
import logging, platform, re, sqlite3, sys

## Third-party imports (Static)

## Global Variable Declarations - CONSTANTS - DO NOT CHANGE @ RUNTIME
## Declare a dictionary to store the possible mimetypes statically.
_mimetype_dict = {\
				1: "email_v2", 2: "im", 3: "nickname", 4: "organization",\
				5: "phone_v2", 6: "sip_address", 7: "name", 8: "postal-address_v2",\
				9: "identity", 10: "photo", 11: "group_membership", 12: "note",\
				13: "contact_misc"\
}

## Validate that the a filename was given.
if (len(sys.argv) != 2):
	print "\n    USAGE: " + sys.argv[0] + " <filename>"
	sys.exit(5)

## Create a connection to the database in the file as well as the cursor object.
db_conn = sqlite3.connect(sys.argv[1])
c = db_conn.cursor()	

## Get the names of all the tables in the database.
c.execute("SELECT name FROM sqlite_master WHERE type='table';")
for each in c.fetchall():
	print str(each[0])

## Get the names of the columns in the contacts database.
c.execute('select * from contacts')
for each in c.description:
	print each[0]

sys.exit()


## Show all of the rows of the mimetypes table.
## This table could be used to dynamically configure the mimetypes.
print "\n==MIMETYPES=="
for row in c.execute('SELECT * FROM mimetypes'):
	print row

## Show all of the rows of the contacts table.
## This table is the simplest way to get raw_id and correlate the information stored in other tables.
print "\n==CONTACTS=="
for row in c.execute('SELECT * FROM contacts'):
	print row

## Show all of the rows of the data table.
## This table contains the actual entries for different types of contact details.
print "\n==DATA=="
for row in c.execute('SELECT * FROM data'):
	print row
