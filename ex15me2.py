from sys import argv

script, filename = argv

txt = open(filename)
print "Your text file is: %r" % filename
print "The contents of your file are:",
print txt.read()
