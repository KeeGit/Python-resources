#importing argv from sys
from sys import argv
#arguments are script and name of file
script, filename = argv
#Will print - We are going to erase the filename
print "We're going to erase %r." %filename
#Will print - If you don't want that, hit ctrl-C
print "If you don't want that, hit CTRL-C (^C)."
#Will print - If you do want that, hit Return
print "If you do want that, hit RETURN."
#Takes input at the prompt
raw_input("?")
#Will print - Opening the file..
print "Opening the file.."
#Target is the name of the open file, and we are opening it in the write mode
target = open(filename, 'w')
#Will print - Truncating the file. Goodbye!
print "Truncating the file. Goodbye!"
#Truncate will empty the file
target.truncate()
#Will print - Now I'm going to as kyou for three lines
print "Now I'm going to ask you for three lines."
#Raw-inputing the 3 lines
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")
#Will print- I'm going to write these to the file.
print "I'm going to write these to the file."
#Write('stuff')- will write to the file
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
#Will print - And finally, we close it.
print "And finally, we close it."
target.close()



