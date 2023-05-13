import pickle

def main():
#BEFORE GAME START
    player_name = input("Enter your character's name: \n")
    inventory = ["", ""]
    player_position = ""
    item1 = "Samurai_katana"
    item2 = "Baseball Bat"
    item3 = "Shotgun"
    item4 = "Key"
    item1_collected = False
    Room5_zombiesgone = False
    Room12_zombiesgone = False
    Room19_zombiesgone = False
    Room27_unlocked = False
   

    controls = ("CONTROLS:\n\nWEST\nEAST\nNORTH\nSOUTH\nPICKUP\nATTACK/USE\nHELP\n")

    Room1 = ("\nYou look around from the car you took to the mall, there are 4 ways you can go. Hallways to your north, west, and east. And south is the exit.")
    Room2 = ("\nAs you enter the room you see it used to be a cafe of some kind, you try one of the machines but it doesn't work. Dang. You decide to get back to your job and see a hallway to the west")
    Room3 = ("\nYou walk into a crossroads, the south is taken out so no going that way. The west leads to an apple store which you're guessing is abandoned, and north leads you to an abandoned office.")
    Room4 = ("\nAs you enter the apple store you see it has already been looted, the technology wouldn't have been any help since it would have been dead. To your west you see an opening to a pretty large room.")
    Room5z = ("\nAs you enter the doorway to your west you see a horde of zombies, with this horde a very sharp weapon would scatter them, but for now you can't go west until you scatter them")
    Room5noz = ("\nYou enter the doorway into a large area where you had scattered zombies earlier.")
    Room6 = ("\nWith the zombies scattered you continue through the large area but see nothing of interest other than a door to your north.")
    Room7_weaponnotcollected = ("\nAs you enter the room you don't see anything, but out of the corner of your eye you see a baseball bat in a barrel")
    Room7 = ("\nWhen you enter the room you see nothing of value.")
    Room8_weaponnotcollected = ("\nYou decide to go north into the office building, and you manage to find a samurai katana. The only way you can go from here is north out the back door, our south through the way you just came.")
    Room8 = ("\nYou decide to go north into the office building. The only way you can go from here is north out the back door, our south through the way you just came.")
    Room9z = ("\nAs you leave through the backdoor, you see a disturbing sight. There is a horde of zombies just ahead of you, this is a small horde and will need a blunt object to move them.")
    Room9noz = ("\nYou enter a deserted hallway you scattered zombies in.")
    Room10 = ("\nAs you go east from your car, you see a long, uninteresting hallway that looks like it goes on for a while.")
    Room11 = ("\nThe long, boring hallway continues on")
    Room12z = ("\nAs you are walking down the long, boring hallway you eventually come upon a massive horde of zombies, you can kill them all with some a powerful weapon like a shotgun.")
    Room12noz = ("\nThe long, boring hallway continues on")
    Room13 = ("\nNow that there aren't any zombies here, you see the boring hallway finally comes to an end in a room just east from where you are, which opens into a hunting store.")
    Room14 = ("\nYou don't see any bullets in the hunting store, but you see a key which looks like it could open a locked door.")
    Room15 = ("\nAs you enter the room from the hallway, you see trash scattered around the area, and traces of zombies. You don't see any zombies near you but it is clear they were here at one point. The building continues north")
    Room16 = ("\nAs you trudge through the long building, you finally come across a door. When you open it you see it opens into something into some other area to your north")
    Room17 = ("\nWhen you open the door, you come upon a massive area, with beautiful statues now covered in moss, you guess this is the center of the mall. There are paths in all directions.")
    Room18 = ("\nThis hallway looks like it once was a beautiful piece of architecture, but now there is greenery covering all of it. It makes it beautiful in a weird way. The hallway continues west or east")
    Room19 = ("\nSince the zombies are scattered, this area is trashed with junk thrown everywhere. This room looks like it could have been a food court in the past. There are hallways south, west, and east.")
    Room20 = ("\nAs you continue enter the room, you can hear some noises coming from a building just west from where you are.")
    Room21_isaacnotsaved = (f"\nAs you enter the store, you see your friend Isaac, '{player_name}! I thought you weren't gonna find me, you must've dealt with the zombies since you made it here. I am gonna go to the car and place my supplies there, see you there!' With Isaac leaving, you see nothing else in this room.")
    Room21_isaacsaved = ("\nAs you enter the room, you see some stray rats scrambling around, how did these rats cause all this ruckus?")
    Room22_weaponnotcollected = ("\nYou decide to go east, and as you are walking across the hallway, you see a shotgun to the right. The hallway continues on East")
    Room22 = ("\nYou decide to go east as the hallway continues")
    Room23 = ("\nYou enter a weird art store, there aren't any paintings that catch your attention, the art room continues east")
    Room24_normal = ("\nYou continue going down the art store until you come to a dead end, with a picture of a man smiling at you, he looks friendly.")
    Room24_trueending = ("\nYou continue going down the art store until you come to the end, where you see a picture of a man smiling at you, he looks friendly.")
    Room25 = ("\nYou decide to go north and come up to an escalator. Well it used to be, now since there isn't power it is basically just a staircase. It continues north.")
    Room26 = ("\nAs you ascend the stairs, they seemed to go on forever. Once you reach the top, to your north you see a locked door. You see that it needs a key to be opened")
    Room27_nokey = ("\nYou can't continue until you find a way through the locked door")
    Room27 = ("\nAs you open the door you come across a beautiful room, untouched by nature with hallways north, east, and west. The north seems to head to a boys bathroom, and the east is a girls bathroom.")
    Room28 = ("\nWhen you enter the room, you realise this is a police department for the mall. You don't find anything of value.")
    Room29 = ("\nWhen you enter the girls bathroom, the only thing there remotely close to a girl are the rats running around.")
    Room30_tazznotsaved = (f"\nAs you enter the bathroom, you hear a massive fart and plop. 'Is that you Tazz?' you call out. All the sudden a stall opens and you see Tazz come out of it. '{player_name}! You got me at a bad time but I was stuck here and needed to do my thing yknow. I actually gathered some food for the colony, I will meet you at the car!'")
    Room30_tazzsaved = ("\nYou enter the boys bathroom and hear a disfunctional toilet constantly flushing, how is that thing still working?")
    Zombies_in_room = ("\nYou can't go this way with zombies right there!")
    Locked_door_room = ("\nYou can't continue until you find a way through this door!")
#GAME START

    print("After some Chinese scientist had a failed experiment, zombies began to appear all throughout the world and cause a meltdown of humanity")
    print("You and some friends managed to make a small colony near NUAMES high-school, but the situation is dire. You are starving and in need of supplies")
    print("You, Tazz, and Isaac were all 'volunteered' to go and get supplies for the colony, you arrived at your destination and while you got to work fixing the car, Isaac and Tazz headed out for supplies")
    print("But then, you got a distress call from Isaac and Tazz, Isaac got cornered by zombies and Tazz locked himself in a room to escape some zombies chasing him, and they both need help, so it is time to save your friends!")
    print(f"{Room1}")
    print("You have no weapons, so you are hoping to find some around the mall.")
    player_position = Room1
    player_input = ""

    room_number = 1
    roomNoZ = False
    room9NoZ = False
    room12NoZ = False
    isaacSaved = False
    tazzSaved = False
    shotgunPickedUp = False
    keyPickedUp = False
    baseballbatPickedUp = False
    katanaPickedUp = False
    ending = False
    ending1 = False
    ending2 = False
    ending3 = False
    ending4 = False
    true_ending = False
    save = [room9NoZ, room12NoZ, isaacSaved, tazzSaved, shotgunPickedUp, keyPickedUp, baseballbatPickedUp, katanaPickedUp, Room5_zombiesgone, Room12_zombiesgone, Room19_zombiesgone, Room27_unlocked, shotgunPickedUp, ending1, ending2, ending3, ending4]
   

    while True:
        if ending == True:
            item1_collected = False
            Room5_zombiesgone = False
            Room12_zombiesgone = False
            Room19_zombiesgone = False
            Room27_unlocked = False
            room9NoZ = False
            room12NoZ = False
            isaacSaved = False
            tazzSaved = False
            shotgunPickedUp = False
            keyPickedUp = False
            baseballbatPickedUp = False
            katanaPickedUp = False
            room_number = 1
            ending = False
        
        player_input = ""
        player_input = input("\nWhat do you want to do?\n").lower()

       
       
       
        if player_input == "save":

            
            f = open("save.txt", "w")
            f.write("") 
            f.close() 
            f = open("save.txt", "a") 
            for i in range(len(save)): 
                  f.write(str(save[i]) + ",") 

            f.close() #close the file

        if player_input == "load":
            f = open("save.txt", "r") 
            line = f.readline()
            f.close() 

            saveLoad = line.split(",")

           
            if saveLoad[0] == "True":
                  room9NoZ = True
            else:
                  room9NoZ = False
            
            if saveLoad[1] == "True":
                  room12NoZ = True
            else:
                  room12NoZ = False
            
            if saveLoad[2] == "True":
                  isaacSaved = True
            else:
                  isaacSaved = False

            if saveLoad[3] == "True":
                  tazzSaved = True
            else:
                  tazzSaved = False

            if saveLoad[4] == "True":
                  shotgunPickedUp = True
            else:
                  shotgunPickedUp = False

            if saveLoad[5] == "True":
                  keyPickedUp = True
            else:
                  keyPickedUp = False

            if saveLoad[6] == "True":
                  baseballbatPickedUp = True
            else:
                  baseballbatPickedUp = False

            if saveLoad[7] == "True":
                  katanaPickedUp = True
            else:
                  katanaPickedUp = False

            if saveLoad[8] == "True":
                  Room5_zombiesgone = True
            else:
                  Room5_zombiesgone = False

            if saveLoad[9] == "True":
                  Room12_zombiesgone = True
            else:
                  Room12_zombiesgone = False

            if saveLoad[10] == "True":
                  Room19_zombiesgone = True
            else:
                  Room19_zombiesgone = False

            if saveLoad[11] == "True":
                  Room27_unlocked = True
            else:
                  Room27_unlocked = False
            
            if saveLoad[12] == "True":
                  ending1 = True
            else:
                  ending1 = False
            
            if saveLoad[13] == "True":
                  ending2 = True
            else:
                  ending2 = False
            
            if saveLoad[14] == "True":
                  ending3 = True
            else: 
                  ending3 = False
            
            if saveLoad[15] == "True":
                  ending4 = True
            else:
                  ending4 = False
       
       
       
       
        if player_input == "quit":
              break
        
        if player_input == "controls":
              print(controls)
        
        if player_input == "command.giveall":
              inventory.append(item1)
              katanaPickedUp = True
              inventory.append(item2)
              baseballbatPickedUp = True
              inventory.append(item3)
              shotgunPickedUp = True
              inventory.append(item4)
              keyPickedUp = True
              print("Given every weapon in the game.")
      
        if player_input == "command.allendings_complete":
              ending1 = True
              ending2 = True
              ending3 = True
              ending4 = True
              print("Given every ending except the true ending!")

        if player_input == "help":
              print("Ending 1: Betrayal\nEnding 2: Betrayal of Tazz\nEnding 3: Betrayal of Isaac\nEnding 4: Good Ending\nEnding 5: True Ending (hint, you need every other ending to get this one!)")

        if player_input == "inventory":
              print(f"{inventory}")
      


        if "room" + str(room_number) == "room1": #Room 1
                if player_input == "north":
                    room_number = 15
                    print(Room15)
                if player_input == "west":
                      room_number = 2
                      print(Room2)
                if player_input == "east":
                      room_number = 10
                      print(Room10)
                if player_input == "south" and isaacSaved == False and tazzSaved == False:
                    print("You decide to leave without either of your friends. You arrive back at the colony and tell them that Tazz and Isaac got captured by zombies. You will never live down the guilt you feel now by leaving your friends behind.\n")
                    print("Congrats! You got Ending 1 of 5; Betrayal.")
                    ending1 = True
                    ending = True
                if player_input == "south" and isaacSaved == True and tazzSaved == False:
                    print("As you are entering the car, Isaac asks 'hey, what about Tazz?' You told him that you were too late to rescue him and he died. Isaac gave a sad expression but said that you should leave as soon as you can. You can never live down the guilt of lying to your best friend and deserting the other.\n")
                    print("Congrats! You got Ending 2 of 5; Tazz Deserted")
                    ending2 = True
                    ending = True
                if player_input == "south" and isaacSaved == False and tazzSaved == True:
                    print("As you start to get in the car, Tazz asks 'Hey, what about Isaac? Are we just gonna leave him?'\nYou told him that Isaac had died by the time you had got there and that you needed to go. Tazz agreed and you both left. You will never live down the guilt of leaving your friend behind.\n")
                    print("Congrats! You got Ending 3 out of 5; Betrayal of Isaac")
                    ending3 = True
                    ending = True
                if player_input == "south" and isaacSaved == True and tazzSaved == True:
                      print("As you arrive back to the car, you see both of your best friends there. You get a good feeling knowing that you saved both of their lives. 'Come on guys, lets get out of here and back to the colony.' Tazz and Isaac agree and you three all head out back to the colony and you still have both of your best friends.")
                      print("Congrats! You got Ending 4 out of 5; Good Ending")
                      ending4 = True
                      ending = True
                if player_input == "pickup":
                      print("you cannot pick anything up here.")
                if player_input == "attack":
                      print("you cannot attack here")

        elif "room" + str(room_number) == "room2": #Room 2
                if player_input == "north":
                    print("you cannot go this way.")
                if player_input == "west":
                      room_number = 3
                      print(Room3)
                if player_input == "east":
                      room_number = 1
                      print(Room1)
                if player_input == "south":
                    print("you cannot go this way.")
                if player_input == "pickup":
                      print("you cannot pick anything up here.")
                if player_input == "attack":
                      print("you cannot attack here")
                
        elif "room" + str(room_number) == "room3": #Room 3
                if player_input == "north":
                    room_number = 8
                    if katanaPickedUp == True:
                        print(Room8)
                    if katanaPickedUp == False:
                          print(Room8_weaponnotcollected)
                if player_input == "west":
                      room_number = 4
                      print(Room4)
                if player_input == "east":
                      room_number = 2
                      print(Room2)
                if player_input == "south":
                    #room_number = 0
                    print("you cannot go this way.")
                if player_input == "pickup":
                      print("you cannot pickup anything here.")
                if player_input == "attack":
                      print("you cannot attack here")
                      
                
        elif "room" + str(room_number) == "room4": #Room 4
                if player_input == "north":
                    #room_number = 8
                    print("You cannot go this way.")
                if player_input == "west":
                      room_number = 5
                      if Room5_zombiesgone == False: 
                        print(Room5z)
                        room_number = 5
                      elif Room5_zombiesgone == True:
                        print(Room5noz)  
                if player_input == "east":
                      room_number = 3
                      print(Room3)
                if player_input == "south":
                    #room_number = 0
                    print("you cannot go this way.")
                if player_input == "pickup":
                      print("you cannot pick anything up here.")
                if player_input == "attack":
                      print("you cannot attack here")
        
        elif "room" + str(room_number) == "room5": #Room 5
                if player_input == "north":
                    #room_number = 8
                    print("You cannot go this way")
                if player_input == "west" and Room5_zombiesgone == False:
                      room_number = 5	
                      print("You can't progress this way until you deal with the zombies.")
                if player_input == "west" and Room5_zombiesgone == True:
                      room_number = 6
                      print(Room6)
                if player_input == "east":
                      room_number = 4
                      print(Room4)
                if player_input == "south":
                    #room_number = 0
                    print("you cannot go this way.")
                if player_input == "pickup":
                      print("you cannot pick anything up here.")
                if player_input == "attack" and katanaPickedUp == True:
                      print("You rush at the zombies with your katana, not knowing how to handle one your form isn't great. But you kill a couple zombies and the rest scatter, allowing you to move on.")
                      Room5_zombiesgone = True
                if player_input == "attack" and katanaPickedUp == False:
                      print("You don't have the correct weapon to attack these zombies.")
                      
                
        elif "room" + str(room_number) == "room6": #Room 6
                if player_input == "north":
                    room_number = 7
                    if item1_collected: 
                        print(Room7) 
                    if not(item1_collected): 
                        print(Room7_weaponnotcollected)
                if player_input == "west":
                      #room_number = 6
                      print("you cannot go this way.")
                if player_input == "east":
                      room_number = 5
                      print(Room5noz)
                if player_input == "south":
                    #room_number = 0
                    print("you cannot go this way.")
                if player_input == "pickup":
                      print("You can't pick up anything here")
                if player_input == "attack":
                      print("you cannot attack here")

        elif "room" + str(room_number) == "room7": #Room 7
                if player_input == "north":
                    #room_number = 0
                    print("You cannot go this way")
                if player_input == "west":
                      #room_number = 0
                      print("you cannot got this way.")
                if player_input == "east":
                      #room_number = 0
                      print("You cannot go this way")
                if player_input == "south":
                    room_number = 6
                    print(Room6)
                if player_input == "pickup" and baseballbatPickedUp == True:
                      print("You already picked up the item in this room.")
                if player_input == "pickup" and baseballbatPickedUp == False:
                      print("As you walk over to the baseball bat, you pick it up. It is old and shoddy, but looks like it will get the job done.")
                      baseballbatPickedUp = True
                      inventory.append(item2)
                if player_input == "attack":
                      print("you cannot attack here")
        
        elif "room" + str(room_number) == "room8": #Room 8
                if player_input == "north":
                    room_number = 9
                    if room9NoZ == False: 
                        print(Room9z)
                    elif room9NoZ == True:
                          print(Room9noz)
                if player_input == "west":
                      #room_number = 0
                      print("You cannot go this way.")
                if player_input == "east":
                      #room_number = 0
                      print("you cannot go this way.")
                if player_input == "south":
                    room_number = 3
                    print(Room3)
                if player_input == "pickup" and katanaPickedUp == True:
                      print("You already picked up the item in this room.")
                if player_input == "pickup" and katanaPickedUp == False:
                      print("As you walk up to the barrel with the katana, you grab it out of the barrel, it shines brightly in the room")
                      katanaPickedUp = True
                      inventory.append(item1)
                if player_input == "attack":
                      print("you cannot attack here")

        elif "room" + str(room_number) == "room9": #Room 9
                if player_input == "north" and Room19_zombiesgone == True:
                    room_number = 19
                    print(Room19)
                if player_input == "north" and Room19_zombiesgone == False:
                      print("You can't go this way until you deal with these zombies")
                if player_input == "west":
                      #room_number = 0
                      print("You cannot go this way.")
                if player_input == "east":
                      #room_number = 0
                      print("You cannot go this way")
                if player_input == "south":
                    room_number = 8
                    print(Room8)
                if player_input == "pickup":
                      print("you cannot pick anything up here.")
                if player_input == "attack" and item2 in inventory:
                      print("You rush the zombies with your bat, and quickly take off some of their heads, forcing them to scatter. The path is now clear")
                      Room19_zombiesgone = True
                      Room9noz = True
                if player_input == "attack" and item2 not in inventory:
                      print("You don't have the correct weapons to deal with these zombies.")

        elif "room" + str(room_number) == "room10": #Room 10
                if player_input == "north":
                    #room_number = 8
                    print("You cannot go this way")
                if player_input == "west":
                      room_number = 1
                      print(Room1)
                if player_input == "east":
                      room_number = 11
                      print(Room11)
                if player_input == "south":
                    #room_number = 0
                    print("you cannot go this way.")
                if player_input == "pickup":
                      print("you cannot pick anything up here.")
                if player_input == "attack":
                      print("you cannot attack here")

        elif "room" + str(room_number) == "room11": #Room 11
                if player_input == "north":
                    #room_number = 0
                    print("You cannot go this way")
                if player_input == "west":
                      room_number = 10
                      print(Room10)
                if player_input == "east":
                      room_number = 12
                      if room12NoZ == False: 
                        print(Room12z)
                      elif room12NoZ == True:
                        print(Room12noz)
                if player_input == "south":
                    #room_number = 0
                    print("you cannot go this way.")
                if player_input == "pickup":
                      print("you cannot pick anything up here.")
                if player_input == "attack": 
                      print("you cannot attack here")

        elif "room" + str(room_number) == "room12": #Room 12
                if player_input == "north":
                    #room_number = 8
                    print("You cannot go this way")
                if player_input == "west":
                      room_number = 11
                      print(Room11)
                if player_input == "east" and Room12_zombiesgone == True:
                      room_number = 13
                      print(Room13)
                if player_input == "east" and Room12_zombiesgone == False:
                      print("You can't go this way until you deal with the zombies")
                if player_input == "south":
                    #room_number = 0
                    print("you cannot go this way.")
                if player_input == "pickup":
                      print("you cannot pick anything up here.")
                if player_input == "attack" and item3 in inventory:
                      print("You cock your shotgun and shoot at the zombies, wiping out hordes of them with a few shots. After seeing so many fall they scatter and run away")
                      Room12_zombiesgone = True
                if player_input == "attack" and item3 not in inventory:
                      print("You don't have the correct weapons to attack.")
        
        elif "room" + str(room_number) == "room13": #Room 13
                if player_input == "north":
                    #room_number = 0
                    print("You cannot go this way")
                if player_input == "west":
                      room_number = 12
                      print(Room12noz)
                if player_input == "east":
                      room_number = 14
                      print(Room14)
                if player_input == "south":
                    #room_number = 0
                    print("you cannot go this way.")
                if player_input == "pickup":
                      print("you cannot pick anything up here.")
                if player_input == "attack":
                      print("you cannot attack here")

        elif "room" + str(room_number) == "room14": #Room 14
                if player_input == "north":
                    #room_number = 0
                    print("You cannot go this way")
                if player_input == "west":
                      room_number = 13
                      print(Room13)
                if player_input == "east":
                      #room_number = 0
                      print("you cannot go this way.")
                if player_input == "south":
                    #room_number = 0
                    print("you cannot go this way.")
                if player_input == "pickup":
                      keyPickedUp = True 
                      print("You picked up the key, it looks like it goes to a locked door.")
                      inventory.append(item4)
                if player_input == "attack":
                      print("you cannot attack here")

        elif "room" + str(room_number) == "room15": #Room 15
                if player_input == "north":
                    room_number = 16
                    print(Room16)
                if player_input == "west":
                      #room_number = 0
                      print("You cannot go this way.")
                if player_input == "east":
                      #room_number = 0
                      print("You cannot go this way.")
                if player_input == "south":
                    room_number = 1
                    print(Room1)
                if player_input == "pickup":
                      print("you cannot pick anything up here.")
                if player_input == "attack":
                      print("you cannot attack here")

        elif "room" + str(room_number) == "room16": #Room 16
                if player_input == "north":
                    room_number = 17
                    print(Room17)
                if player_input == "west":
                      #room_number = 0
                      print("You cannot go this way.")
                if player_input == "east":
                      #room_number = 0
                      print("You cannot go this way.")
                if player_input == "south":
                    room_number = 15
                    print(Room15)
                if player_input == "pickup":
                      print("you cannot pick anything up here.")
                if player_input == "attack":
                      print("you cannot attack here")
        
        elif "room" + str(room_number) == "room17": #Room 17
                if player_input == "north":
                    room_number = 25
                    print(Room25)
                if player_input == "west":
                      room_number = 18
                      print(Room18)
                if player_input == "east":
                      room_number = 22
                      if shotgunPickedUp == False: 
                        print(Room22_weaponnotcollected)
                      elif shotgunPickedUp == True:
                        print(Room22)
                if player_input == "south":
                    room_number = 16
                    print(Room16)
                if player_input == "pickup":
                      pass 
                if player_input == "attack":
                      print("you cannot attack here")

        elif "room" + str(room_number) == "room18": #Room 18
                if player_input == "north":
                    #room_number = 8
                    print("You cannot go this way")
                if player_input == "west" and room9NoZ == False:
                      print("There are zombies blocking the road! You need a blunt object to pass these zombies.")
                if player_input == "west" and room9NoZ == True:
                      room_number = 19
                      print(Room19)
                if player_input == "east":
                      room_number = 17
                      print(Room17)
                if player_input == "south":
                    #room_number = 0
                    print("you cannot go this way.")
                if player_input == "pickup":
                      print("you cannot pick anything up here.")
                if player_input == "attack" and item2 in inventory:
                      print("You rush the zombies with the baseball bat, quickly taking a few of their heads off. After this destruction the zombies flee in many directions, opening the way forward.")
                      room9Noz = True
                      Room19_zombiesgone = True
                if player_input == "attack" and item2 not in inventory:
                      print("You don't have the correct weapon to defeat the zombies!")

        elif "room" + str(room_number) == "room19": 
                if player_input == "north":
                    #room_number = 8
                    print("You cannot go this way")
                if player_input == "west":
                      room_number = 20
                      print(Room20)
                if player_input == "east":
                      room_number = 18
                      print(Room18)
                if player_input == "south":
                    room_number = 9
                    print(Room9noz)
                if player_input == "pickup":
                      print("you cannot pick anything up here.")
                if player_input == "attack":
                      print("you cannot attack here")
        
        elif "room" + str(room_number) == "room20": #Room 20
                if player_input == "north":
                    #room_number = 0
                    print("You cannot go this way")
                if player_input == "west":
                      room_number = 21
                      if isaacSaved == True:
                            print(Room21_isaacsaved)
                      if isaacSaved == False: 
                        print(Room21_isaacnotsaved)
                        isaacSaved = True
                if player_input == "east":
                      room_number = 19
                      print(Room19_zombiesgone)
                if player_input == "south":
                    #room_number = 0
                    print("you cannot go this way.")
                if player_input == "pickup":
                      print("you cannot pick anything up here.")
                if player_input == "attack":
                      print("you cannot attack here")

        elif "room" + str(room_number) == "room21": #Room 21
                if player_input == "north":
                    #room_number = 0
                    print("You cannot go this way")
                if player_input == "west":
                      #room_number = 0
                      print("You cannot go this way")
                if player_input == "east":
                      room_number = 20
                      print(Room20)
                if player_input == "south":
                    #room_number = 0
                    print("you cannot go this way.")
                if player_input == "pickup":
                      print("you cannot pick anything up here.")
                if player_input == "attack":
                      print("you cannot attack here")

        elif "room" + str(room_number) == "room22": #Room 22
                if player_input == "north":
                    #room_number = 8
                    print("You cannot go this way")
                if player_input == "west":
                      room_number = 17
                      print(Room17)
                if player_input == "east":
                      room_number = 23
                      print(Room23)
                if player_input == "south":
                    #room_number = 0
                    print("you cannot go this way.")
                if player_input == "pickup" and shotgunPickedUp == True:
                      print("You already picked up the item in this room.")
                if player_input == "pickup" and shotgunPickedUp == False:
                      print("You walk over and pickup the shotgun. It looks pretty old but it looks like it is still working.")
                      shotgunPickedUp = True
                      inventory.append(item3)
                if player_input == "attack":
                      print("you cannot attack here")

        elif "room" + str(room_number) == "room23": #Room 23
                if player_input == "north":
                    #room_number = 0
                    print("You cannot go this way")
                if player_input == "west":
                      room_number = 22
                      print(Room22)
                if player_input == "east":
                      room_number = 24
                      print(Room24_normal)
                if player_input == "east" and ending1 == True and ending2 == True and ending3 == True and ending4 == True:
                      print("As you enter the room, you see a painting at the end glowing very bright, it looks like a portal you can enter!\n") 
                if player_input == "south":
                    #room_number = 0
                    print("you cannot go this way.")
                if player_input == "pickup":
                      print("you cannot pick anything up here.")
                if player_input == "attack":
                      print("you cannot attack here")

        elif "room" + str(room_number) == "room24": #Room 24
                if player_input == "north":
                    #room_number = 0
                    print("You cannot go this way")
                if player_input == "west":
                      room_number = 23
                      print(Room23)
                if player_input == "east" and ending1 == True and ending2 == True and ending3 == True and ending4 == True:
                      print(f"As you step into the portal, you get blinded. You start to panic as you don't know what is going on until all the sudden you fall asleep.\nWhen you wake up you look around and you see a man standing in front of you. 'God?' you ask to the figure.\nThe figure would turn around and reveal himself to be Mr. Simonsen, your old programming teacher. 'Congrats {player_name}, you beat the simulation!' (type 'continue' to continue on with the dialogue)")
                      if player_input == "continue":
                              print("'Simulation?' you ask him. 'Yes, everything you see here is just a simulation to see what you would do during the apocalypse! Your input is greatly appreciated.' You look around and pinch yourself\nAll the sudden you wake up in a fully white room with a bunch of scientists looking at you.")
                              print("Congrats! You have gotten Ending 5 of 5; True Ending")
                              print("Thank you for playing!")
                              break
                if player_input == "east" and ending1 == False or ending2 == False or ending3 == False or ending4 == False:
                      #room_number = 0
                      print("You cannot go this way.")
                if player_input == "south":
                    #room_number = 0
                    print("you cannot go this way.")
                if player_input == "continue" and ending1 == True and ending2 == True and ending3 == True and ending4 == True:
                        print("'Simulation?' you ask him. 'Yes, everything you see here is just a simulation to see what you would do during the apocalypse! Your input is greatly appreciated.' You look around and pinch yourself\nAll the sudden you wake up in a fully white room with a bunch of scientists looking at you.\n")
                        print("Congrats! You have gotten Ending 5 of 5; True Ending")
                        print("Thank you for playing!")
                        break
                if player_input == "pickup":
                      print("you cannot pick anything up here.")
                if player_input == "attack":
                      print("you cannot attack here")

        elif "room" + str(room_number) == "room25": #Room 25
                if player_input == "north":
                    room_number = 26
                    print(Room26)
                if player_input == "west":
                      #room_number = 0
                      print("You cannot go this way.")
                if player_input == "east":
                      #room_number = 0
                      print("You cannot go this way.")
                if player_input == "south":
                    room_number = 17
                    print(Room17)
                if player_input == "pickup":
                      print("you cannot pick anything up here.")
                if player_input == "attack":
                      print("you cannot attack here")

        elif "room" + str(room_number) == "room26": #Room 26
                if player_input == "north":
                    if Room27_unlocked == False: 
                          print(Room27_nokey)
                    elif Room27_unlocked == True:
                          room_number = 27
                          print(Room27)
                if player_input == "west":
                      #room_number = 0
                      print("You cannot go this way.")
                if player_input == "east":
                      #room_number = 0
                      print("You cannot go this way.")
                if player_input == "south":
                    room_number = 25
                    print(Room25)
                if player_input == "pickup":
                      print("you cannot pick anything up here.")
                if player_input == "attack":
                      print("You decide to use logic and try to kick the door down. Since it is rusted you take it down and continue on.")
                      Room27_unlocked = True
                if player_input == "use" and item4 in inventory:
                      print("You use the key and successfully unlock the door allowing you to continue.")
                      Room27_unlocked = True
                  

        elif "room" + str(room_number) == "room27": #Room 27
                if player_input == "north":
                    room_number = 30
                    if tazzSaved == True:      
                          print(Room30_tazzsaved)                   
                    elif tazzSaved == False:
                          print(Room30_tazznotsaved)
                          tazzSaved = True
                if player_input == "west":
                      room_number = 28
                      print(Room28)
                if player_input == "east":
                      room_number = 29
                      print(Room29)
                if player_input == "south":
                    #room_number = 0
                    print("you cannot go this way.")
                if player_input == "pickup":
                      pass 
                if player_input == "attack":
                      print("you cannot attack here")

        elif "room" + str(room_number) == "room28": #Room 28
                if player_input == "north":
                    #room_number = 0
                    print("You cannot go this way")
                if player_input == "west":
                      #room_number = 0
                      print("You cannot go this way.")
                if player_input == "east":
                      room_number = 27
                      print(Room27)
                if player_input == "south":
                    #room_number = 0
                    print("you cannot go this way.")
                if player_input == "pickup":
                      print("you cannot pick anything up here.")
                if player_input == "attack":
                      print("you cannot attack here")

        elif "room" + str(room_number) == "room29": #Room 29
                if player_input == "north":
                    #room_number = 0
                    print("You cannot go this way")
                if player_input == "west":
                      room_number = 27
                      print(Room27)
                if player_input == "east":
                      #room_number = 0
                      print("You cannot go this way.")
                if player_input == "south":
                    #room_number = 0
                    print("you cannot go this way.")
                if player_input == "pickup":
                      print("you cannot pick anything up here.")
                if player_input == "attack":
                      print("you cannot attack here")

        elif "room" + str(room_number) == "room30": #Room 30
                if player_input == "north":
                    #room_number = 0
                    print("You cannot go this way")
                if player_input == "west":
                      #room_number = 0
                      print("You cannot go this way.")
                if player_input == "east":
                      #room_number = 0
                      print("You cannot go this way.")
                if player_input == "south":
                    room_number = 27
                    print(Room27)
                if player_input == "pickup":
                      print("you cannot pick anything up here.")
                if player_input == "attack":
                      print("you cannot attack here")
       
      
#go to 7

#EXAMPLE OBJECT
#class Example:
     # def __init__(self, name, age):
           # self.name = name
            #self.age = age

     # def greet(self):
            #print(f"Hello, my name is {self.name} and I'm {self.age} years old.")

#obj = Example("John", 30)

#print(obj.name)
#print(obj.age)

#obj.greet()





if __name__ == "__main__":
		main()
