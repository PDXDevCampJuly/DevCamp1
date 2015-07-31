# This is a maze program #### make a search function to find object or person in
# a room with a closed door and can only open it with obtained object . yell at
# them if user doesn't have said object

###########################

# description: a description of the current room
# doors: dictionary with door:location sets

pudding = True
def process_user_movement(description, actions):
  # print the description of the current room
  print(description)

  # print the available doors
  print("You have some choices. What do you do?: ")
  for each_action in actions:
    print("*", each_action)
  # prompt the for what doors they want
  userInput = input("Choose: ").title()

  # do things based on user response
  while True:
    try:
      actions[userInput]()
      break
    # invalid response: ask them again
    except KeyError:
      userInput = input("Invalid input, try again: ").title()




# def search_user_object(description, object):
#     print(description_object)
#     print("Do you wish to temporarily satisfy your hunger?:")
#     for each_pudding in puddings:
#         print("*", each_pudding)
#     userInput  = input("Eat or Pass?:").title()
#     while True:
#         try:
#           pudding[userInput]()
#           break
#       except:
#           userInput = input("Invalid input, try again: ").title()


def room1():
  global pudding
  description = """\nYou are in ROOM ONE\n
The East door smells of Roses. The South door smells of Basil."""
  if pudding:
      description += "\nYou see a big bowl of delicious chocolate pudding in the middle of the room."

  actions = {"East": room2, "South": room3, "Scarf Pudding": breakthroughDoor}
  process_user_movement(description, actions)

def room2():
  description = """\nYou are in ROOM TWO\n
The West door smells like your grandmother. The South door smells of Fennel."""
  actions = {"West": room1, "South": room4}
  process_user_movement(description, actions)

def room3():
  description = """\nYou are in ROOM THREE\n
The North door smells like your grandmother. The East door smells like Paprika."""
  actions = {"North": room1, "East": room4}
  process_user_movement(description, actions)

def room4():
  description = """\nYou are in ROOM FOUR\n
The North door smells like old plastic.The South door smells like grilled onions.
The West door smells like Paprika."""
  actions = {"North": room2, "South": room5, "West": room3}
  process_user_movement(description, actions)

def room5():
  description = """\nYou are in ROOM FIVE\n
The North door smells like Lilac and Roses. The West door smells of Spaghetti
with Basil-Mint meatballs."""
  actions = {"North": room4, "West": theEnd}
  process_user_movement(description, actions)


def breakthroughDoor():
    global pudding
    print("""\nYou have chosen to eat the pudding and you are feeling
incredibly bright eyed and bushy tailed, not to mention strong!""")
    pudding = False
    description = """\nYou are in ROOM ONE\n
The East door smells of Roses. The South door smells of Basil. There is no
more pudding since you scarfed it down.\n"""
    actions = {"East": room2, "South": room3}
    process_user_movement(description, actions)

###trying to figure out how you can enter in a passcode "hidden" to take you straight to the end
#def roomhidden():
#    print("You found the hidden passage! Clearly you have a nose for a-maze-ing things!")

def theEnd():
  global pudding
  if pudding:
    actions =  {"Go Back": room5}
    description = """\nYou're too weak. You can't open this door unless you gain energy.
Go back and eat that pudding, Goober!\n"""
    process_user_movement(description, actions)
  else:
      print("\nWHEW! What a sniffer! You sure know how to put your nose to the grindstone!\n")



  #if pudding has been eaten then the west door in room 5 can be opened
  #if pudding hasn't been eaten then the west door saysr


def start():
  print("""
\nYou suddenly realize you've stumbled upon a maze that
reminds you of your grandmother's house.  You are incredibly hungry
and the only way out is to follow your nose!  So get sniffing!""")
  room1()

start()
