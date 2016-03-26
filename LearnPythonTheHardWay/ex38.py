# variable = string
ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there are not 10 things in that list. Let's fix that"

#new variable = split string ucalling split(' ')
#more_stuff is a list
#ten_things.split('') - will split ten_things, where there is a space, and will insert a commas
#split(ten_things)
stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]
#len(stuff) - will find the length of stuff
for i in stuff:
	if len(stuff) != 10:
		next_one = more_stuff.pop() #more_stuff.pop() = pop(more_stuff)
		print "Adding: ", next_one
		stuff.append(next_one) #stuff.append(next_one) = will append next_one to stuff.
		print "There are %d items now." %len(stuff)
	else:
		break
	
print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1] #Will print index 1 in stuff
print stuff[-1] #whoa! fancy #will print index -1 in stuff
print stuff.pop() #pop(stuff) -function is pop, and stuff is argument.
print ' '.join(stuff) # what? cool! #join function will remove the commas between the arguments, and joins the elements of the string
print '#'.join(stuff[3:5]) #super stellar! #Will join arguments between 3 and 5, by inserting a #
#join(stuff) - function is join, argument is stuff.
