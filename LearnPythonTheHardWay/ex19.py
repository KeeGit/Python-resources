#We are defining the function, cheese_and_crackers,and giving the arguments- cheese_count, boxes_of_crackers to the function.
def cheese_and_crackers(cheese_count, boxes_of_crackers):
#The following print statements will be printed everytime we call this function.
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crakers!" %boxes_of_crackers
	print "Man, that's enough for a party!"
	print "Get a blanket. \n"
	
#We are in the script now, not in the function.	
print "We can just give the function numbers directly:"
#We are assigning numbers directly to the function.
cheese_and_crackers(20,30)

#We are assigning variables from our script to the function, and calling it
print "Or, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)
#We are assigning numbers directly to the function and even doing math inside it.
print "We can even do math inside too:"
cheese_and_crackers(10+20, 5+6)
#We are combining variables and math and calling the function.
print "And we can combine the two, varibales and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
#When we print this code, everytime the cheese_and_crackers function is called, the whole code for the function is printed.