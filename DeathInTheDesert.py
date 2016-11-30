# coding: utf-8
print 'Hello!/n'
print "Welcome to Death in Desert\n"

#select name
name = raw_input("What name will you be choosing for this deathly adventure?")
print "Alright, %s, let's die in the desert. \n" % (name)
print "\n\n\n"
#ADVENTURE BEGINS

print "Your plane has crashed in the desert. You are the only survivor. You have two bottles of water, one sheet, and one blanket. What do you do?\n"
print "A) Start walking\n"
print "B) Curl into a ball and cry\n"
answer1 = raw_input()
if answer1 == "b":
	print "You dehydrate yourself beyond help and die of thirst. \n YOU HAVE DIED!"
if answer1 == "a":
	print "You start walking. After about half an hour, the sand is burning your feet. You can:\n"
	print "A) Tear the sheet to make shoes\n"
	print "B) Keep walking\n"
	answer2 = raw_input()
	if answer2 == "b":
		print "After a few hours, you collapse, exhausted and burned. You never wake up. \n YOU HAVE DIED!"
	if answer2 == "a":
		print "You keep walking, wearing your makeshift shoes. You become very thirsty. You can: \n"
		print "A) Drink all your water\n"
		print "B) Drink a little bit and keep walking \n"
		answer3 = raw_input()
		if answer3 == "a":
			print "You drink all of your water and keep walking, but then you dehydrate and have no more water. \n YOU HAVE DIED!"
		if answer3 == "b":
			print "You keep walking, but then a rattlesnake bites you. You don't know how to cure it. \n YOU DIE!"
		
