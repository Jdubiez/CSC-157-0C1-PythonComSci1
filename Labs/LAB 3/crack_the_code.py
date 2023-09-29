# **************************************************************************
# * Name: Jahson Westby                                             CSC 157
# * Date: 9-28-23                                                     LAB 3
# *************************************************************************
# * Problem Statement and Specifications:
# * Ask user if  for their name, if they are ready then get their inputs for Phase 1-3
# * if number is correct then move onto the next phase, if not tell them they are wrong
# *
# * Input:
# * name
# * phase 1 number
# * phase 2 number
# * phase 3 number
# * Output:
# * correct or incorrect statements
# *
# *************************************************************************

# Get users name
name = str(input("Welcome. What is your name?\n")).title()

# Find out if users are ready to crack the code
ready = str(
    input("Hello " + str(name) + ". Are you ready to crack the code?\n")
).upper()

# I was too lazy to write this multiple times
def right():
    print("Correct!")
def wrong():
    print("Sorry, that was incorrect!\nBetter luck next time!")

# If user is ready
if ready == "YES":

    # Phase 1
    phase1 = int(input("\nPHASE 1\nEnter a number:\n"))
    if phase1 == 3:
        right()

        # Phase 2
        phase2 = int(input("\nPHASE 2\nEnter a number:\n"))
        if phase2 == 1 or 33 <= phase2 <= 100:
            right()

            # Phase 3
            phase3 = int(input("\nPHASE 3\nEnter a number:\n"))
            if phase3 > 0 and (phase3 % 3 == 0 or phase3 % 7 == 0):
                right()
                print("You have cracked the code!")
                
# Output if user is wrong
            else:
                wrong()
        else:
            wrong()
    else:
        wrong()

