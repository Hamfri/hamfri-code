from sys import argv

script, filename = argv

print "Your text file name is %r.Is this the text file you want to edit???"% filename
txt = open(filename,'w')

print "Are you sure that you want to delete the contents of %r?? "% filename

print "And now we are deleting the contents.....Goodbye!!!"
txt.truncate()

print "please answer the following questions to add new content to your text file"

line1 = raw_input("Whats your name?")
line2 = raw_input("What is your favourite meal??")
line3 =raw_input("Where did you spend your chrismas holiday??")

txt.write(line1)
txt.write("\t")
txt.write(line2)
txt.write("\n")
txt.write(line3)

print "Thank you for taking your time to answer my questions"
print "Goodbye!!!"

txt.close()
