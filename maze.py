#start  print description
#       prompt input with valid exits
#           valid - act on input
#
#           else - reprompt (invalid)
#       print description
###############


def start():
    print("Welcome to your life.")

    room0()

def process_user_movement(description, doors):
    # print description of the current room
    print(description)

    # print  the available doors

    # prompt which door they want
    # do thing based on response: go to the correct location

    #  invalid response: ask them again

def room0():
    # description
    description = """You suddenly find yourself in a room. Exits are East and South. One way leads you to ever-lasting life.
    The other leads to sudden death. Which way do you want to go? East or South?"""
    # doors
    # where those doors go
    doors = {"East":room1}

    process_user_movement(description, doors)

def room1():
    #description = ""
    pass

def room2():
    pass

def room3():
    pass

def room4():
    pass

def room5():
    pass
