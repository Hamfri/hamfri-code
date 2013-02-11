num = 0
elements = []

while num < 6:
     print "The number at the top is %d" % num
     
     elements.append(num)
     num += 1
     print "Numbers now: ", elements
     print "The number at the bottom is %d" % num
     
for num in elements:
   print "This is number: %d" % num     
