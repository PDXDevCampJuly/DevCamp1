from Wk3_mon_die import Die #I've already made a Die class, so I'm importing the function from this file(module) so I can call its functions
from angry_dice import Angrydice# from my module(file) I'm importing my Angrydice class so I can call all its functions
die_a = Angrydice()#die_a is equal to what has been set from the Angrydice class so I can make a die_a
die_b = Angrydice()#die_b is equal to what has been set from the Angrydice class so I can make a die_b
cheating = False #making cheating variable equal false so I can use a global function within another function for a sudo short-cut
current_stage = 1#making  current_stage variable so I can use a global function within another function for a sudo short-cut

def user_roll(die_a, die_b):# these are the 2 objects that I will be manipulating in the game
    global cheating# this is to allow a check in the cheating function

    print("""You rolled:
        a = [  {}  ]
        b = [  {}  ]

        You are in Stage {}""".format(die_a.currentValue, die_b.currentValue, current_stage))
        #the curly brackets allow the currentValue of both die to be "let in" and shown as well as the current_stage

    userInput = input("Roll dice:")#input allows the user to do something
    #if  userInput[] - check if its a , b,


    if current_stage == 3: #this is to check a cheating function during stage_Three because you can't lock in the 6
        if "a" not in userInput: #this says that if the user doesn't select "a" and the value equals 6...
            if die_a.value == 6:# and the value is equal to 6...
                print("HA! That is cheating. Roll again!")
                cheating = True#then the cheater is caught!
        if "b" not in userInput:#this says that if the user doesn't select "a" and the value equals 6...
            if die_b.value == 6:#and the value is equal to 6...
                print("HA! That is cheating. Roll again!")
                cheating = True#then the cheater is caught!


    if "a" in userInput: #this function is indicating the users input if they choose "a"...
        die_a.roll()#then use the roll function for die_a
    if "b" in userInput:#this function is indicating the users input if they choose "b"...
        die_b.roll()#then use the roll function for die_b



def stage_One():#this function describes what the valaues have equal(or what the user rolls) before moving onto the next stage
    global current_stage #calling my variable from the top having set it to 1
    # user must roll until:

    user_roll(die_a, die_b)#this calls the user_roll function for die_a and die_b
    check_angry()#this calls my check angry function on whether or not the function starts over to stage_One
    #if die_a or die_b equals 1, or 2
        #then user holds either die_a or die_b
    #return user_roll to roll again
    if die_a.value + die_b.value == 3: #this function states that if the value of both dice are equal to the set value, then you "win" that stage
        #when user decides to hold both
        #return user_roll with updated Stage Two

        current_stage += 1#this takes the current_stage and adds 1 to it so it increases the stages you are currently in




def stage_Two():#this function describes what the valaues have equal(or what the user rolls) before moving onto the next stage
    global current_stage #calling my variable from the top having set it to 1
    #use must roll until:
    user_roll(die_a, die_b)#this calls the user_roll function for die_a and die_b
    check_angry()#this calls my check angry function on whether or not the function starts over to stage_One

    if die_a.value + die_b.value == 7: #this function states that if the value of both dice are equal to the set value, then you "win" that stage

        current_stage += 1#this takes the current_stage and adds 1 to it so it increases the stages you are currently in
            #then user decides to hold both
            #proceed to stage_Three


def stage_Three():#this function describes what the valaues have equal(or what the user rolls) before moving onto the next stage
    global current_stage #calling my variable from the top having set it to 1

    user_roll(die_a, die_b)#this calls the user_roll function for die_a and die_b
    check_angry()#this calls my check angry function on whether or not the function starts over to stage_One


        #if die_a or die_b equals 5, or 6
            #then user holds either die_a or die_b only if it's a 5
            #if user tries to hold 6 first
            # call them a cheater
            # return user_roll
        #return user_roll to roll again
    if die_a.value + die_b.value == 11 and not cheating:#this function indicates that
    #if the values of both dice equals 11 and cheating hasn't occured then it prints out your score and declares the user WINNER!
        print("""You rolled:
            a = [  {}  ]
            b = [  {}  ]

                """.format(die_a.currentValue, die_b.currentValue))
        current_stage +=1#this takes the current_stage and adds 1 to it so it increases the stages you are currently in
        winner()#this runs the winner function
    #when a and b are held
        #then user WINS "You've won! Calm Down!"
            #exit game

def check_angry():#this function check to see if the user should be kicked back to stage_One
    global current_stage# taken from my set variable at the top
    if die_a.value == 3 and die_b.value == 3:#this function checks to see if both Angry die have been rolled and yells at user to calm down
        print("WOAH! Enhance your calm, John Spartan. Go back to stage 1!")
        current_stage = 1#not sure why this is here is I pulled the global statement...


def winner():#this function declares a winner!

    print("You've won! Calm down!")




def start_game():#this function starts the gae with a description of how to play and tells users to press Enter to start
    input("""Welcome to Angry Dice! Roll the two dice until you get thru the 3 Stages!
    Stage 1 you need to roll 1 & 2
    Stage 2 you need to roll ANGRY & 4
    Stage 3 you need to roll 5 & 6
    You can lock a die needed for your current stage
    and just roll the other one, but beware!
    If you ever get 2 ANGRY's at once, you have to restart to Stage 1!
    Also, you can never lock a 6! That's cheating!

    To roll the dice, simply input the name of the die you want to roll.
    Their names are a and b.

    Press ENTER to start!""")


start_game()#this calles the start_game function

while current_stage != 4:#stage 4 is technically or meta-"ly" the winner stage
    if current_stage == 1:#this fucntion says that is current stage is equal to 1...
        stage_One()#then the stage_One function is called
    if current_stage == 2:#this fucntion says that is current stage is equal to 2...
        stage_Two()#then the stage_Two function is called
    if current_stage == 3:#this fucntion says that is current stage is equal to 3...
        stage_Three()#then the stage_Three function is called




#this is a test function for user_roll passing in given values to test
#user_roll(1,Die([2,3]),Die([5,1]))
