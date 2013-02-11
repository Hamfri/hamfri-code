from sys import argv

script, first, second, third, fourth = argv
x = raw_input("input first argument?")
y = raw_input("input second  argument?")
z = raw_input("input third argument?")
w = raw_input("input fourth argument?")

print "The script is called %r Your first argument is %r ,your second argument is %r ,your third argument is %r ,your fourth argument is %r"%(script, x, y, z, w)
