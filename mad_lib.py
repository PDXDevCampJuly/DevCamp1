# This comment will be ignored by Python.
# Comments are good for people reading your script and knowing what it's about.
#################

article = "So "

theInput = input("Please type a number greater than 1. >>")

article = article + theInput + " guys walk into a "

theInput = input("Please type a solid object. >>")
article = article + theInput + ". The bartender laughs and "
# short cut   article += theInput + ". The baetender laughs and "

theInput = input("Please type an action verb. >>")
article = article + theInput + " a bowl of "

theInput = input("Please type squishy object. >>")
article = article  + theInput + " through the air as he shouts "

theInput = input("Please type exuberant saying of excitement. >>")
article = article + theInput + "! Then the guys decide to "

theInput = input("Please type a verb.  >>")
article = article + theInput + "!"

print ("\n\n") #\n means a new line
print (article)
print ("\n\n")
