# we are inputting a string as age
age = raw_input("How old are you?")
# we are inputing a string as height
height = raw_input ("How tall are you?")
#we are inputing a string as weight
weight =raw_input ("What is your weight?")
# Will print - So, you are __ old, __tall and ___ heavy.
print "So, you are %r old, %r tall and %r heavy." %(age, height, weight)



from sys import argv

script, first, second, third = argv

# Will print - The script is called:script
print "The script is called:", script
#Will print-Your first variable is: first
print "Your first variable is:", first
#Will print- Your second variable is: second
print "Your second variable is:", second
# Will print - Your third variable is: third
print "Your third variable is:", third