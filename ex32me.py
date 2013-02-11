likes = ['pilau', 'chips', 'Grilled chicken', 'Fruit salads', 'Fruit juices']

# the following loop prints elements in a list
for goodies in likes:
   print "I love %s" % goodies
   
# Next we create a list and populate it using the append methods
elements = []
for i in range(0, 10):
   print "Populating %d in the list" % i
   elements.append(i)
   
# and finally we display the elements that have been injected into the list
for i in elements:
   print "This is element number: %d in the list" % i
