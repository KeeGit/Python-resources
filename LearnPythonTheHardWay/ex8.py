# var = " format characters"
formatter = "%r %r %r %r"

# Will print 1,2,3,4
print formatter %(1,2,3,4)
# print "%r %r %r %r" %(1, 2, 3, 4) - This is normally how I would print the above statement. 
#Will print - one, two, three, four
print formatter %("one", "two", "three", "four")
#Will print - True, False, False, True
print formatter %(True, False, False, True)
# Will print %r %r %r %r four times
print formatter %(formatter, formatter, formatter, formatter)
#Will print - I had this thing. That you could type up right. But it didn't sing. So I said good night. I didnot understand why it printed these statements with quotes. Looks like strings entered with " " are printed with ' '
print formatter %(
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)