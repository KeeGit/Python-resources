#this is import argv from sys
from sys import argv
#script, filename are the arguments
script, filename = argv
# variable txt will open the filename, using the open()
txt = open(filename)
#Will print - Here's your file ex15_sample.txt
print "Here's your file %r:" %filename
#txt.read() will the contents of the file
print txt.read()
#Will print-Type the filename again: 
print "Type the filename again:"
#A > will apear, and we have to type the file name
file_again = raw_input(">")
# opened file is assigned to txt_again
txt_again = open(file_again)
#Will print the file
print txt_again.read()
