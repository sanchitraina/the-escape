# test commit
from sys import argv, exit

script, op_list1, op_list2, op_list3 = argv

path = ['bumpy road', 'cheering crowd and roaring engines', '3 flights of stairs']
objects_in_room = ['A glass bottle on a table', 'A burning candle']

final_op_dark_room = []
final_op_corridor = []
final_op_ground_floor = []

prompt = "> "

def caught():
	print "Hit RETURN to exit"
	raw_input(prompt)
	exit(0)

def invalid():
	print "Invalid choice. Rot in peace!"
	caught()

def proceed():
	print "Hit RETURN to proceed"
	raw_input(prompt)

def to_list(arg1, arg2, arg3):
	
		op_dark_room = open(arg1)
		option_dark_room = op_dark_room.readlines()
		op_dark_room.close()
		for i in option_dark_room:
			final_op_dark_room.append(i.strip())
	
		op_corridor = open(arg2)
		option_corridor = op_corridor.readlines()
		op_corridor.close()
		for i in option_corridor:
			final_op_corridor.append(i.strip())
	
		op_ground_floor = open(arg3)
		option_ground_floor = op_ground_floor.readlines()
		op_ground_floor.close()
		for i in option_ground_floor:
			final_op_ground_floor.append(i.strip())

to_list(op_list1, op_list2, op_list3)

def escape_ground_floor(list3):
	print """
	You are on the ground floor now and the guards know that you have escaped from the room.
	You notice that you are near a small race track, there is a crowd cheering, an unattended car and a race is going on.
	What do you do next?
	"""
	
	for i in range(0, 2):
		print i + 1, list3[i]
	
	choice = raw_input(prompt)
	
	if choice == "1":
		print """
		You see the guards looking for you. You notice a race car pull up and it's door is open.
		You sneak through the crowd and enter the car and run away by it.
		By the time guards are aware of this, you have gone too far from them.
		Congratulations! You are a free person now.
		Hit RETURN for the final time to exit the game.
		"""
		raw_input(prompt)
		exit(0)
	
	elif choice == "2":
		print """
		You ran towards the car and drew attention to yourself.
		The guards caught you.
		You were so close to escaping, if you hadn't been this greedy.
		Better luck next time.
		"""
		caught()
	
	else:
		invalid()

def escape_corridor(list2):
	print "You are in the corridor now. You need to get out before the other guards notice that you are gone."
	print "There are 3 ways you can go"
	for i in range(0, 3):
		print i + 1, list2[i]
	print "What do you do next?"
	
	choice = raw_input(prompt)
	
	if choice == "1":
		print """
		You enter an empty room and you see a closed window.
		You open it and look out to notice that there is a pipe adjacent to it. You climb down that pipe. 
		A guard enters that open room and notices the open window and you climbing down the pipe.
		"""
		proceed()
		escape_ground_floor(final_op_ground_floor)
	elif choice == "2":
		print "You take the stairs and when you reach to the ground floor, you notice that the exit is guarded."
		print "Fortunately there is a back door and no one is guarding it."
		print "You sneak up to it and open it. It squeeks and the guard at the other exit sees you trying to escape."
		proceed()
		escape_ground_floor(final_op_ground_floor)
	elif choice == "3":
		print "As soon as the elevator door opens, a group of guards comes out and they again restrain you."
		caught()
	else:
		invalid()

def escape_dark_room(list1):
	
	print "What do you do next?"
	
	for i in range(0, 2):
		print i + 1, list1[i]
	
	choice = raw_input(prompt)
	
	if choice == '1':
		print "The guard outside gets alerted and he stops you. He takes out everything from the room. Rot in peace!"
		caught()
	elif choice == '2':
		print "You've burned the rope and broken free. Great job"
		proceed()
	else:
		invalid()
	
	print """
			Now that you've broken free, you need to get out of the room.
			There is only one way out and that is through the door.
			What do you do next?
		  """
	
	for i in range (2, 5):
		print i - 1, list1[i]
	
	temp = True
	
	while temp:
		choice = raw_input(prompt)
	
		if choice == "1":
			print "You've got the guard's attention, he is thinking about coming inside."
			temp = False
			proceed()
		elif choice == "2":
			print """
				The guard  had the keys to unlock the room and he is unconscious now.
				You don't have any way to open the door now. The other guards sees this and again ties your hands.
				"""
			caught()
		elif choice == "3" and temp:
			print "The guards change shifts. You need to do something else."
		else:
			invalid()
	
	print "What do you do next?"
	
	for i in range(5, 7):
		print i - 4, list1[i]
	
	choice = raw_input(prompt)
	
	if choice == '1':
		print "The guard is a trained MMA fighter. He kicks your ass and ties you again."
		caught()
	elif choice == '2':
		print """
			The guard looks through the door viewer and he doesn't see you there.
			He enters, you push him inside from the behind and lock the room from outside.
			"""
		proceed()
		escape_corridor(final_op_corridor)
	else:
		invalid()

def dark_room(var2):
	print "Your kidnapper takes off the cloth that was covering your face and you find yourself in a dark room with no windows"
	print "After getting a grip, you notice a few things in the room."
	for i in range (0, len(var2)):
		print i + 1, var2[i]
	print "'You will rot here for the rest of your life' said the kidnapper looking at you."
	print "Surely you don't have any plans to do that."
	print "Hit RETURN and plan your escape"
	raw_input(prompt)
	escape_dark_room(final_op_dark_room)

def journey(var1):
	print "\n After some time you gain consciousness..."
	print "You are in a car and you notice that your hands are tied and face covered."
	print "You observe that you are going through a %s." % var1[0]
	print "After some time the car stops and you hear %s" % var1[1]
	print "You feel that there are 3 men with you who take you up %s" % var1[2]
	print "Hit RETURN to continue."
	raw_input(prompt)
	dark_room(objects_in_room)

def start():
	print """
	You are enjoying a nice weekend lunch when you hear a knock on the door.
	You go to open the door and see a strange looking man standing there.
	He immediately sprays something on your face and you become unconscious.
	Press RETURN to find out what happens next
	"""
	raw_input(prompt)
	journey(path)

start()