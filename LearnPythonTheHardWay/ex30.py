people = 30
cars = 40
trucks = 15


if cars > people: #Condition met. Print statement.
	print "We should take the cars."
elif cars < people: #Condition not met. Statement, not printed.
	print "We should not take the cars."
else: #One of the if statement's is met. So else statement will not be printed.
	print "We can't decide."

if trucks > cars: #Condition not met. Statement not printed.
	print "That's too many trucks."
elif trucks < cars: #Condition met. Statement will be printed.
	print "Maybe we could take the trucks."
else: #One of the conditions met.Else condition will not be executed.
	print "We still can't decide"

if people > trucks: #Condition met. Statement will be printed.
	print "Alright, let's just take the trucks."
else: #The if condition is met, so else statement will not be printed.
	print "Fine, let's stay home then."
