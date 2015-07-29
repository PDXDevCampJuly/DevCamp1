# This is a maze program
###########################

# description: a description of the current room
# doors: dictionary with door:location sets
def process_user_movement(description, doors):
  # print the description of the current room
  print(description)

  # print the available doors
  print("Which door do you choose?: ")
  for each_door in doors:
    print("*", each_door)
  # prompt the for what doors they want
  userInput = input("Choose a door: ").title()

  # do things based on user response
  while True:
    # valid response: go to the correct location
    try:
      doors[userInput]()
      break

    # invalid response: ask them again
    except:
      userInput = input("Invalid input, try again: ").title()

def room1():
  description = """\nYou are in ROOM ONE -
  The East door smells of Roses. The South door smells of Basil."""
  doors = {"East": room2, "South": room3}
  process_user_movement(description, doors)

def room2():
  description = """\nYou are in ROOM TWO -
  The West door smells like your grandmother. The South door smells of Fennel."""
  doors = {"West": room1, "South": room4}
  process_user_movement(description, doors)

def room3():
  description = """\nYou are in ROOM THREE
  The North door smells like your grandmother. The East door smells like Paprika."""
  doors = {"North": room1, "East": room4}
  process_user_movement(description, doors)

def room4():
  description = """\nYou are in ROOM FOUR
  The North door smells like old plastic.The South door smells like grilled onions.
  The West door smells like Paprika."""
  doors = {"North": room2, "South": room5, "West": room3}
  process_user_movement(description, doors)

def room5():
  description = """\nYou are in ROOM FIVE
  The North door smells like Lilac and Roses. The West door smells of Spaghetti with Basilmint meatballs."""
  doors = {"North": room4, "West": theEnd}
  process_user_movement(description, doors)

### trying to figure out how you can enter in a passcode "hidden" to take you straight to the end
#def roomhidden():
#    print("You found the hidden passage! Clearly you have a nose for a-maze-ing things!")

def theEnd():
  print("\nWHEW! What a sniffer! You sure know how to put your nose to the grindstone!\n")



def start():
  print("""\nYou suddenly realize you've stumbled upon a maze that reminds you of your grandmother's house.
  You are incredibly hungry and the only way out is to follow your nose! So get sniffing!""")
  room1()

start()
