def start():
   print "You are in the dark room."
   print "There is a door to your right and left."
   print "Which one do you take?"
   
   next = raw_input("> ")
   
   if next == "left":
     bear_room()
   elif next == "right":
       cthulu_room()
   else:
       dead("You stumble around the room until you starve.")
       
       
start()   
