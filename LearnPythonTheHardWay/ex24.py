#Will print - Let's practice everything.
print "Let's practice everything."
#Will print - You'd need to know 'bout escapes with \ that do 
# newlines and 	tabs.
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of lovely
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""
#Will print ------------
# 	The lovely world
#with logic so firmly planted
#cannot discern
# the needs of lovely
#nor comprehend passion from intuition
#and requires an explanation
#		where this is none.
#------------
print "------------"
print poem
print "------------"


five = 10 - 2 + 3 -6
#Will print - This should be five: 5
print "This should be five: %s" %five
#Defined a function called secret_formula, with an argument called - started, it will run thru the formula and return the variables with computed values
def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans, jars, crates

#creating a variable called start_point, and assigning it a value	
start_point = 10000
#Calculated the value of beans,jars and crates using secret_formula,argument started is assigned variable start_point
beans, jars, crates = secret_formula(start_point)
#Will print - With a starting point of 10000
print "With a starting point of: %d" % start_point
#Will print -We'd have 5000000 beans, 5000 jars, and 50 crates.
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)
#We gave a new value to start_point
start_point = start_point / 10
#We can also do that this way:
print "We can also do that this way:"
#We'd have 500000 beans, 500 jars, and 5 crates.
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)


