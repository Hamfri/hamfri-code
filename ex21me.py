def add(a, b):
   print "Adding %d + %d" % (a, b)
   return a + b
   
def subtract(a, b):
   print "Subtracting %d - %d" % (a, b)
   return a - b
   
Rblood = add(100, 50)
Wblood = subtract(100, 50)
print "Your Red blood cells are: %d,Your White blood cells are: %d" % (Rblood,Wblood)

what = add(Rblood, subtract(Wblood, 2))  
print what 
