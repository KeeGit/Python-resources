#importing argv from sys
from sys import argv
#importing exists from os.path
from os.path import exists
#arguments of argv are script, from_file, to_file
script, from_file, to_file = argv
# Will print copying from from_file to to_file
print "Copying from %s to %s" %(from_file, to_file)

#we could do these two on one line, how? indata=from_file.read()
in_file = open(from_file)
indata = in_file.read()
#%d is len(indata)
print "The input file is %d bytes long" % len(indata)
# checking if the output file exists using the exists()-O/p will be true/False
print "Does the output file exist? %r" % exists(to_file)
#Python recognizes Return and CTRL-C
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()
#out_file - will open the file to be copied to
out_file = open(to_file, 'w')
#writing in the out_file, the indata
out_file.write(indata)

print "Alright, all done."

out_file.close()
in_file.close()