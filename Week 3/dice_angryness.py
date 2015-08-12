from Wk3_mon_die import Die
from angry_dice import Angrydice
die_a = Angrydice()
die_b = Angrydice()
cheating = False
current_stage = 1

def user_roll(die_a, die_b):
    global cheating

    print("""You rolled:
        a = [  {}  ]
        b = [  {}  ]

        You are in Stage {}""".format(die_a.currentValue, die_b.currentValue,current_stage))

    userInput = input("Roll dice:")
    #if  userInput[] - check if its a , b, a


    if current_stage == 3:
        if "a" not in userInput:
            if die_a.value == 6:
                print("HA! That is cheating. Roll again!")
                cheating = True
        if "b" not in userInput:
            if die_b.value == 6:
                print("HA! That is cheating. Roll again!")
                cheating = True


    if "a" in userInput:
        die_a.roll()
    if "b" in userInput:
        die_b.roll()



def stage_One():
    global current_stage
    # user must roll until:

    user_roll(die_a, die_b)
    check_angry()
    #if die_a or die_b equals 1, or 2
        #then user holds either die_a or die_b
    #return user_roll to roll again
    if die_a.value + die_b.value == 3:
        #when user decides to hold both
        #return user_roll with updated Stage Two

        current_stage += 1


#if two "Angry" are rolled while any die are held then immediately start over to the beginning of stage_One


def stage_Two():
    global current_stage
    #use must roll until:
    user_roll(die_a, die_b)
    check_angry()



    #if die_a or die_b equals ANGRY or 4
        #then user holds either die_a or die_b
    #return user_roll to roll again
    if die_a.value + die_b.value == 7:
        current_stage += 1
            #then user decides to hold both
            #proceed to stage_Three







def stage_Three():
    global current_stage
    #    #use must roll until:
    user_roll(die_a, die_b)
    check_angry()
    

        #if die_a or die_b equals 5, or 6
            #then user holds either die_a or die_b only if it's a 5
            #if user tries to hold 6 first
            # call them a cheater
            # return user_roll
        #return user_roll to roll again
    if die_a.value + die_b.value == 11 and not cheating:
        print("""You rolled:
            a = [  {}  ]
            b = [  {}  ]

                """.format(die_a.currentValue, die_b.currentValue))
        current_stage +=1
        winner()
    #when a and b are held
        #then user WINS "You've won! Calm Down!"
            #exit game

def check_angry():
    global current_stage
    if die_a.value == 3 and die_b.value == 3:
        print("WOAH! Enhance your calm, John Spartan. Go back to stage 1!")
        current_stage = 1


def winner():

    print("You've won! Calm down!")




def start_game():
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


start_game()

while current_stage != 4:
    if current_stage == 1:
        stage_One()
    if current_stage == 2:
        stage_Two()
    if current_stage == 3:
        stage_Three()





#user_roll(1,Die([2,3]),Die([5,1]))
