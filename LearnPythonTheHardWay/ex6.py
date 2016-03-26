# Assisgning a string with a format character to a variable
x = "There are % d types of people." %10
# Here we are assigning a string to a variable
binary = "binary"
# Here we are assigning a string to a variable
do_not = "don't"
# Here we are putting a string inside a string using %s.
y = "Those who know %s and those who %s." %(binary,do_not)
# Printing a string
print x
# Printing a string
print y
# Here we are inserting a string inside a string
print "I said: %r." %x
# Here too we are inserting a string inside a string
print "I also said: '%s'." %y
# We are assigning a boolean to a variable
hilarious = False
# So we can also assign a string to a variable, and have a format character with no value assigned to it
joke_evaluation = "Isn't that joke so funny?! %r"
# We are not having a " " for joke_evaluation as it is a variable, and it has a format character
print joke_evaluation %hilarious
# variable = "string"
w = "This is the left side of ..."
#variable = "string"
e = "a string with a right side."
# we can add two variables
print w+e
