# Here's some new strange stuff, remember type it exactly.
#var ="string"
days = "Mon Tue Wed Thu Fri Sat Sun"
#var = "string- with each string printed in a new line"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"
# Will print - Here are the days: Mon Tue Wed Thu Fri Sat Sun. Strings with format charactes are not printed with ' ''
print "Here are the days: ", days
# Will print Here are the months: Jan..Feb Mar etc all in a new line
print "Here are the months: ", months
# With 3 quotation marks it prints everything as is. If I changed it to single quotation marks, it prints the same thing. The single and double quotation marks can be used interchangeably.
print '''There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
'''