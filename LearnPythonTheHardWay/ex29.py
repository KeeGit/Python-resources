people = 20
cats = 30
dogs = 15


if people < cats: #Condition met, 20 people is less than 30 cats. Will print the statement.
	print "Too many cats! The world is doomed!"
	
if people > cats: #Condition not met. Will not print this statement.
	print "Not many cats! The world is saved!"

if people < dogs: #Condition not met, will not print.
	print "The world is drooled on!"
	
if people > dogs: #Condition met. Will print.
	print "The world is dry!"
	
	
dogs += 5 #dogs = dogs + 5. Dogs = 20

if people >= dogs: #Condition met. Will print.
	print "People are greater than or equal to dogs."
	
if people <= dogs: #Condition met. Will print.
	print "People are less than or equal to dogs."
	

if people == dogs:
	print "People are dogs."
	