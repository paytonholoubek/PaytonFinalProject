def main():
#BEFORE GAME START
	player_name = input("Enter your character's name: \n")
	inventory = ["", ""]
	player_position = ""
	item1 = "Samurai_katana"
	item1_collected = False
	Room5_zombiesgone = False

	controls = ("CONTROLS:\n\nWEST\nEAST\nNORTH\nSOUTH\nPICKUP\nATTACK\n")

	Room1 = ("You look around from the car you took to the mall, there are 4 ways you can go. Hallways to your north, west, and east. And south is the exit.")
	Room2 = ("As you enter the room you see it used to be a cafe of some kind, you try one of the machines but it doesn't work. Dang. You decide to get back to your job and see a hallway to the west")
	Room3 = ("You walk into a crossroads, the south is taken out so no going that way. The west leads to an apple store which you're guessing is abandoned, and north leads you to an abandoned office.")
	Room4 = ("As you enter the apple store you see it has already been looted, the technology wouldn't have been any help since it would have been dead. To your west you see an opening to a pretty large room.")
	Room5z = ("As you enter the doorway to your west you see a horde of zombies, you know a few bullets will make them scatter and allow you to move on, but for now you can't go west until you get those bullets")
	Room5noz = ("You enter the doorway into a large area where you had scattered zombies earlier.")
	Room6 = ("With the zombies scattered you continue through the large area but see nothing of interest other than a door to your north.")
	Room7_weaponnotcollected = ("As you enter the room you don't see anything, but out of the corner of your eye you see a baseball bat in a barrel")
	Room7 = ("When you enter the room you see nothing of value.")
	Room8_weaponnotcollected = ("You decide to go north into the office building, and you manage to find a samurai katana. The only way you can go from here is north out the back door, our south through the way you just came.")
	Room8 = ("You decide to go north into the office building. The only way you can go from here is north out the back door, our south through the way you just came.")
	Room9z = ("As you leave through the backdoor, you see a disturbing sight. There is a horde of zombies just ahead of you, but you can scatter them with a couple of bullets.")
	Room9noz = ("You enter a deserted hallway you scattered zombies in.")
	Room10 = ("As you go east from your car, you see a long, uninteresting hallway that looks like it goes on for a while.")
	Room11 = ("The long, boring hallway continues on")
	Room12z = ("As you are walking down the long, boring hallway you eventually come upon a small horde of zombies, you can kill them all with some bullets.")
	Room12noz = ("The long, boring hallway continues on")
	Room13 = ("Now that there aren't any zombies here, you see the boring hallway finally comes to an end in a room just east from where you are, which opens into a hunting store.")
	Room14 = ("You don't see any bullets in the hunting store, but you see a key which looks like it could open a locked door.")
	Room15 = ("As you enter the room from the hallway, you see trash scattered around the area, and traces of zombies. You don't see any zombies near you but it is clear they were here at one point. The building continues north")
	Room16 = ("As you trudge through the long building, you finally come across a door. When you open it you see it opens into something into some other area to your north")
	Room17 = ("When you open the door, you come upon a massive area, with beautiful statues now covered in moss, you guess this is the center of the mall. There are paths in all directions.")
	Room18 = ("This hallway looks like it once was a beautiful piece of architecture, but now there is greenery covering all of it. It makes it beautiful in a weird way. The hallway continues west or east")
	Room19 = ("Since the zombies are scattered, this area is trashed with junk thrown everywhere. This room looks like it could have been a food court in the past. There are hallways south, west, and east.")
	Room20 = ("As you continue going west, you can hear some noises coming from a building just west from where you are.")
	Room21_isaacnotsaved = (f"As you enter the store, you see your friend Isaac, '{player_name}! I thought you weren't gonna find me, you must've dealt with the zombies since you made it here. I am gonna go to the car and place my supplies there, see you there!' With Isaac leaving, you see nothing else in this room.")
	Room21_isaacsaved = ("As you enter the room, you see some stray rats scrambling around, how did these rats cause all this ruckus?")
	Room22_weaponnotcollected = ("You decide to go east, and as you are walking across the hallway, you see a shotgun to the right. The hallway continues on East")
	Room22 = ("You decide to go east as the hallway continues")
	Room23 = ("You enter a weird art store, there aren't any paintings that catch your attention, the art room continues east")
	Room24_normal = ("You continue going down the art store until you come to a dead end, with a picture of a man smiling at you, he looks friendly.")
	Room24_trueending = ("You continue going down the art store until you come to the end, where you see a picture of a man smiling at you, he looks friendly.")
	Room25 = ("You decide to go north and come up to an escalator. Well it used to be, now since there isn't power it is basically just a staircase. It continues north.")
	Room26 = ("As you ascend the stairs, they seemed to go on forever. Once you reach the top, to your north you see a locked door. You see that it needs a key to be opened")
	Room27_nokey = ("You can't continue until you find a way through the locked door")
	Room27 = ("As you open the door you come across a beautiful room, untouched by nature with hallways north, east, and west. The north seems to head to a boys bathroom, and the east is a girls bathroom.")
	Room28_weaponnotcollected = ("As you enter the room, you realise this is a police department for the mall, you see a baton hanging up on the wall")
	Room28_weaponcollected = ("When you enter the room, you realise this is a police department for the mall.")
	Room29 = ("When you enter the girls bathroom, the only thing there remotely close to a girl are the rats running around.")
	Room30_tazznotsaved = (f"As you enter the bathroom, you hear a massive fart and plop. 'Is that you Tazz?' you call out. All the sudden a stall opens and you see Tazz come out of it. '{player_name}! You got me at a bad time but I was stuck here and needed to do my thing yknow. I actually gathered some food for the colony, I will meet you at the car!'")
	Room30_tazzsaved = (f"You enter the boys bathroom and hear a disfunctional toilet constantly flushing, how is that thing still working?")
	Zombies_in_room = ("You can't go this way with zombies right there!")
	Locked_door_room = ("You can't continue until you find a way through this door!")
#GAME START

	print("After some Chinese scientist had a failed experiment, zombies began to appear all throughout the world and cause a meltdown of humanity")
	print("You and some friends managed to make a small colony near NUAMES high-school, but the situation is dire. You are starving and in need of supplies")
	print("You, Tazz, and Isaac were all 'volunteered' to go and get supplies for the colony, you arrived at your destination and while you got to work fixing the car, Isaac and Tazz headed out for supplies")
	print("But then, you got a distress call from Isaac and Tazz, Isaac got cornered by zombies and Tazz locked himself in a room to escape some zombies chasing him, and they both need help, so it is time to save your friends!")
	print(f"{Room1}")
	print("You have no weapons, so you are hoping to find some around the mall.")
	player_position = Room1
	player_input = ""
	while "q" not in player_input:
		player_input = input("What do you want to do?\n").lower()

		if player_input == "north" and player_position == Room1:
			player_position = Room15
			print(f"{player_position}")
		elif player_input == "north" and player_position == Room15:
			player_position = Room16
			print(f"{player_position}")
		elif player_input == "north" and player_position == Room16:
			player_position = Room17
			print(f"{player_position}")
		elif player_input == "controls":
			print(f"\n{controls}")
		
		
		elif player_input == "west" and player_position == Room1:
			player_position = Room2
			print(f"{player_position}")
		elif player_input == "west" and player_position == Room2:
			player_position = Room3
			print(f"{player_position}")
		elif player_position == Room3:
			if player_input == "east":
				player_position = Room2
				print(f"{player_position}")
			elif player_input == "north" and item1_collected == False:
				player_position = Room8_weaponnotcollected
				print(f"{player_position}")
			elif player_input == "north" and item1_collected == True:
				player_position = Room8
				print(f"{player_position}")
			elif player_input == "west":
				player_position = Room4
				print(f"{player_position}")
			else:
				print("You can't go that way.")
		elif player_input == "pickup" and player_position == Room8_weaponnotcollected:
			player_position = Room8
			print("You walk over and pick up the katana in the barrel, it shines brightly in the room.")
			item1_collected = True
			inventory.append(item1)
		elif player_input == "south" and player_position == Room8 or Room8_weaponnotcollected:
			player_position = Room3
			print(f"{player_position}")
		elif player_input == "west" and player_position == Room4:
			player_position = Room5z
			print(f"{player_position}")
		elif player_input == "west" and player_position == Room5z and Room5_zombiesgone == False:
			print(f"{Zombies_in_room}")


		





if __name__ == "__main__":
		main()
