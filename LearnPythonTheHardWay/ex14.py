from sys import argv
# the arguments are script, user_name
script, user_name, age = argv
#assigning a string > to prompt
prompt = 'Write here:'
#Will print -Hi user_name, I'm the ex14.py script.
print "Hi %s,and I'm %r years old, I'm the %s script." %(user_name, age, script)
#Will print - the text below
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" %user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" %(likes, lives, computer)