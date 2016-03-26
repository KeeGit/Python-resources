#We are importing argv from sys
from sys import argv
#We are specifying the arguments for argv
script, input_file = argv
#We are defining a function called print_all, with a variable called f. We will be print f,as we are calling read on it.
def print_all(f):
	print f.read()
#We are defining a function called rewind, and by calling seek(), we will be going to the beginning of the file, f
def rewind(f):
	f.seek(0)
#We are defining a function called print_a_line, with 2 variables -line_count,f. readline() will read a file, one line at a time.
def print_a_line(line_count,f):
	print line_count, f.readline()
#variable current_file will open input file
current_file = open(input_file)

print "First, let's print the whole file: \n"
#Calling print_all
print_all(current_file)

print "Now let's rewind, kind of like a tape."
#Calling rewind
rewind(current_file)

print "Let's print three lines:"
#Calling a variable inside the function, print_a_line. The variable current_line = line_count, and f is current_file
current_line = 1
print_a_line(current_line,current_file)
#Can also write it as, current_line += 1
current_line =current_line + 1
print_a_line(current_line, current_file)
#Can also write it as current_line += 1
current_line = current_line + 1
print_a_line(current_line, current_file)
