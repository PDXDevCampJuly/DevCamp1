from Wk3_mon_die_test import Die  #I've already made a Die class, so I'm importing the function from this file(module) so I can call its functions
from angry_dice_test import Angrydice# from my module(file) I'm importing my Angrydice class so I can call all its functions

class AngryDiceGame:

    def __init__(self):
        self.die_a = Angrydice()#die_a is equal to what has been set from the Angrydice class so I can make a die_a
        self.die_b = Angrydice()#die_b is equal to what has been set from the Angrydice class so I can make a die_b
        self.cheating = False #making cheating variable equal false so I can use a global function within another function for a sudo short-cut
        self.current_stage = 1#making  current_stage variable so I can use a global function within another function for a sudo short-cut

    def user_roll(self):# these are the 2 objects that I will be manipulating in the game
        print("""You rolled:
            a = [  {}  ]
            b = [  {}  ]

            You are in Stage {}""".format(self.die_a.currentValue, self.die_b.currentValue, self.current_stage))
            #the curly brackets allow the currentValue of both die to be "let in" and shown as well as the current_stage

        userInput = input("Roll dice:")#input allows the user to do something
        #if  userInput[] - check if its a , b,

        return userInput



    def roll(self, userInput):
        if "a" in userInput: #this function is indicating the users input if they choose "a"...
            self.die_a.roll()#then use the roll function for die_a
        if "b" in userInput:#this function is indicating the users input if they choose "b"...
            self.die_b.roll()#then use the roll function for die_b

    def cheat_check(self, userInput):
        self.cheating = False
        if "a" not in userInput: #this says that if the user doesn't select "a" and the value equals 6...
            if self.die_a.value == 6: # and the value is equal to 6...
                print("HA! That is cheating. Roll again!")
                self.cheating = True #then the cheater is caught!
        if "b" not in userInput: #this says that if the user doesn't select "a" and the value equals 6...
            if self.die_b.value == 6: #and the value is equal to 6...
                print("HA! That is cheating. Roll again!")
                self.cheating = True  #then the cheater is caught!


    def stage_One(self):#this function describes what the valaues have equal(or what the user rolls) before moving onto the next stage


        #if die_a or die_b equals 1, or 2
            #then user holds either die_a or die_b
        #return user_roll to roll again
        if self.die_a.value + self.die_b.value == 3: #this function states that if the value of both dice are equal to the set value, then you "win" that stage
            #when user decides to hold both
            #return user_roll with updated Stage Two

            self.current_stage += 1#this takes the current_stage and adds 1 to it so it increases the stages you are currently in




    def stage_Two(self):#this function describes what the valaues have equal(or what the user rolls) before moving onto the next stage



        if self.die_a.value + self.die_b.value == 7: #this function states that if the value of both dice are equal to the set value, then you "win" that stage

            self.current_stage += 1#this takes the current_stage and adds 1 to it so it increases the stages you are currently in
                #then user decides to hold both
                #proceed to stage_Three


    def stage_Three(self):#this function describes what the valaues have equal(or what the user rolls) before moving onto the next stage




            #if die_a or die_b equals 5, or 6
                #then user holds either die_a or die_b only if it's a 5
                #if user tries to hold 6 first
                # call them a cheater
                # return user_roll
            #return user_roll to roll again
        if self.die_a.value + self.die_b.value == 11 and not self.cheating: #this function indicates that
        #if the values of both dice equals 11 and cheating hasn't occured then it prints out your score and declares the user WINNER!
            print("""You rolled:
                a = [  {}  ]
                b = [  {}  ]"""
                  .format(self.die_a.currentValue, self.die_b.currentValue))
            self.current_stage +=1#this takes the current_stage and adds 1 to it so it increases the stages you are currently in
            self.winner()#this runs the winner function
        #when a and b are held
            #then user WINS "You've won! Calm Down!"
                #exit game

    def check_angry(self):#this function check to see if the user should be kicked back to stage_One

        if self.die_a.value == 3 and self.die_b.value == 3: #this function checks to see if both Angry die have been rolled and yells at user to calm down
            print("WOAH! Enhance your calm, John Spartan. Go back to stage 1!")
            self.current_stage = 1 #not sure why this is here is I pulled the global statement...


    def winner(self):#this function declares a winner!

        print("You've won! Calm down!")




    def start_game(self):#this function starts the game with a description of how to play and tells users to press Enter to start
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

    def main(self):

        self.start_game() #this calls the start_game function
        while self.current_stage != 4: #stage 4 is technically or meta-"ly" the winner stage
            userInput = self.user_roll(self.die_a, self.die_b) #this calls the user_roll function for die_a and die_b

            if self.current_stage == 3: #this is to check a cheating function during stage_Three because you can't lock in the 6
                self.cheat_check(userInput)

            self.roll(userInput)

            self.check_angry()

            if self.current_stage == 1: #this fucntion says that is current stage is equal to 1...
                self.stage_One() #then the stage_One function is called
            elif self.current_stage == 2: #this fucntion says that is current stage is equal to 2...
                self.stage_Two() #then the stage_Two function is called
            elif self.current_stage == 3: #this fucntion says that is current stage is equal to 3...
                self.stage_Three() #then the stage_Three function is called


if __name__ == '__main__':
    angrygame = AngryDiceGame()
    angrygame.main()

    #this is a test function for user_roll passing in given values to test
    #user_roll(1,Die([2,3]),Die([5,1]))
