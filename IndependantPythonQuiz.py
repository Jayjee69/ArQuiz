# Title: Arkansas Quiz
# Author: Ja.Y
# Description: My first Python project

import time
import os 

#creating color "variables"

os.system("cls") #use this for windows. change to os.system("clear") for linux

COLORS = {\
"black":"\u001b[30;1m",
"red": "\u001b[31;1m",
"green":"\u001b[32m",
"yellow":"\u001b[33;1m",
"blue":"\u001b[34;1m",
"magenta":"\u001b[35m",
"cyan": "\u001b[36m",
"white":"\u001b[37m",
"yellow-background":"\u001b[43m",
"black-background":"\u001b[40m",
"cyan-background":"\u001b[46;1m",
}

#replacing all color words with its given ansi 

def colorText(text):
    for color in COLORS:
        text = text.replace("[[" + color + "]]", COLORS[color])
    return text

 #printing out my ASCII file
print("""
 
 
 
               d8888          .d88888b.           d8b          
              d88888         d88P" "Y88b          Y8P          
             d88P888         888     888                       
            d88P 888 888d888 888     888 888  888 888 88888888 
           d88P  888 888P"   888     888 888  888 888    d88P  
          d88P   888 888     888 Y8b 888 888  888 888   d88P   
         d8888888888 888     Y88b.Y8b88P Y88b 888 888  d88P    
        d88P     888 888      "Y888888"   "Y88888 888 88888888 
                                  Y8b                        
                                                     
""")

# Starting the greetings block

name = input("\nWelcome to my arkansas quiz, What is your name? ")

time.sleep(.5)

playing = input("\nHello, " + name + "\n\nWould you like to start? ")

if (playing.lower() == "yes") or (playing.lower() == "y"):
    print("\nOkay! Let's play :)\n")
else:
    print("\nToo bad MOM\n")
    
time.sleep(2)

# Starting the Quiz

score = 0

answer = input("What is the capitol of Arkansas?\n A: Little Rock\n B: Jonesboro\n C: Fayetteville\n D: Texarkana\n Answer: ")
if (answer.lower() == "little rock") or (answer.lower() == "a"): 
    print("\nCorrect!\n")
    score+=1
else:
    print("\nINCORRECT\n\nThe correct answer was\n A: Little Rock\n") 
    
time.sleep(1)


answer = input("What is the Arkansas State Beverage?\n A: Beer\n B: Milk\n C: Moon Shine\n D: Orange Juice\n Answer: ")
if (answer.lower() == "milk") or (answer.lower() == "b"):
    print("\nCorrect!\n")
    score+=1
else:
    print("\nNOPE!\n\nThe correct answer was\n B: Milk\n") 

time.sleep(1)

answer = input("What has the  highest elevation in Arkansas at 2,753 feet?\n A: Mount Nebo\n B: Mount Magazine\n C: Rich Mountain\n D: Shinall Mountain\n Answer: ")
if (answer.lower() == "mount magazine") or (answer.lower() == "b"):
    print("\nCorrect!\n")
    score+=1
else:
    print("\nWRONG ANSWER!\n\nThe correct answer was\n B: Mount Magazine\n") 
    
time.sleep(1)

answer = input("Arkansas borders which US State to the South?\n A: Texas\n B: Oklahoma\n C: Tennessee\n D: Louisiana\n Answer: ")
if (answer.lower() == "louisiana") or (answer.lower() == "d"):
    print("\nCorrect!\n")
    score+=1
else:
    print("\nYOU THOUGHT!\n\nThe correct answer was\n D: Louisiana\n") 
    
time.sleep(1)

answer = input("What city was Bill Clinton, the 42nd President of the U.S. born?\n A: Fayetteville\n B: Little Rock\n C: Hope\n D: Jonesboro\n Answer: ")
if (answer.lower() == "hope") or (answer.lower() == "c"):
    print("\nCorrect!\n")
    score+=1
else:
    print("\nSIKE!\n\nThe correct answer was\n C: Hope\n") 
    
time.sleep(1)

answer = input("What is the Arkansas State American Folk Dance?\n A: Barn Dance\n B: Quadrille\n C: Line Dance\n D: Square Dance\n Answer: ")
if (answer.lower() == "square dance") or (answer.lower() == "d"):
    print("\nCorrect!\n")
    score+=1
else:
    print("\nHAHA no\n\nThe correct answer was\n D: Square Dance\n") 

time.sleep(1)

answer = input("Where does Arkansas rank compared to the other states in population?\n A: 27th\n B: 23rd\n C: 22nd\n D: 32nd\n Answer: ")
if (answer.lower() == "27th") or (answer.lower() == "a"):
    print("\nCorrect!\n")
    score+=1
else:
    print("\nNOPE!\n\nThe correct answer was\n A: 27th\n") 

time.sleep(1)

answer = input("What is the Arkansas Sate Flower?\n A: Carnation\n B: Apple Blossom\n C: Iris\n D: Peach Blossom\n Answer: ")
if (answer.lower() == "apple blossom") or (answer.lower() == "b"):
    print("\nCorrect!!\n")
    score+=1
else:
    print("\nWRONG\n\nThe correct answer was\n B: Apple Blossom\n") 

time.sleep(1)

answer = input("What is the Arkansas State Insect?\n A: Bumble Bee\n B: Praying Mantus\n C: Honeybee\n D: Bowl Weevil\n Answer: ")
if (answer.lower() == "honeybee") or (answer.lower() == "c"):
    print("\nCorrect!\n")
    score+=1
else:
    print("Nope\n\nThe correct answer was\n C: Honeybee\n\nLast Chance!\n") 

time.sleep(1)

answer = input("What is the Arkansas State Tree?\n A: Douglas Fir\n B: Pine\n C: Spruce\n D: Valley Oak\n Answer: ")
if (answer.lower() == "pine") or (answer.lower() == "b"):
    print("\nCorrect!\n")
    score+=1
else:
    print("\nEEEGHHHHHH!!\n\nThe correct answer was\n B: Pine\n") 
    
time.sleep(1)

# Gives score out of /10 and also gives percentage grade and ends program
    
print("You got " + str(score) + " questions correct, \nor\n" + str((score / 10) * 100) + "% ")


print("\n  THANKS FOR PLAYING!")

time.sleep(60)

