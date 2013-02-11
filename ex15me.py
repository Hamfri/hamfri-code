from sys import argv

script, filename = argv

txt = open(filename)

print "Your filename is %r:" % filename
print txt.read()

file_again = raw_input("$")

nkt_again = open(file_again)

print nkt_again.read()
