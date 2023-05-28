print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

first_choice = input("To start off our adventure you must choose which path to take. \nOn the left you will find a path that leads through the foggy dark forest which is rummored \nto be haunted by the souls of the dead.\nOn the right you will find a path that goes through a rainfores which is fulles with amazing \nscenery and lovely wild life.\n\nWhat is your choice? Left or Right? ")

first_choice.lower()
if first_choice == "right":
    print("\n\nYou have made a wise decision!\n")
    choice = input("You have traveled almost all the way through the rainforest, but just before you \nare able to leave it you spot a rare Rainforest Frog. You have a choice of picking it up in order \nto better admire it's colors or leaving it alone. \nTouch or Leave? ")
    choice.lower()
    if choice=="touch":
        print("/nYour curiosity got the best of you! /n/nUnfortunantly the frog you decided to touch turned out to be poisonus. \nThe poison was very deadly and you were killed in just a few secconds.")
    elif choice=="leave":
        print("By the time you left the raiforest it had already gotten pretty dark and you needed to find a place to spend the night.\n")
        choice = input("In the vally right outside of the rainforest were 3 houses. \nThe one on the left was a reddish house which belonged to an elderly woman. \nThe one one the right was a larger house which belonged to the local butcher. \nThe house in the middle was a yellow house that belonged to young bussines man.\n\nWhich house will you choose? Left, Middle or Right? ")
        choice.lower()
        if choice=="left":
            print("\nThe elderly woman offered to cook you a warm homemade meal which you gladly accepted. \nAfter some time you started to feel dizzy and lose consciousness. \nTurns out that the elderly woman was a murderer who poisened and killed you. \n\nYou are dead. \nGAME OVER")
        elif choice=="middle":
            print("\nYou have heart to heart conversation over dinner with the butcher. \nIn the morning while getting ready to leave he comes to thank you for the pleasant \nconversation and gives you a rare vintage necklace which is rumored to grant wishes of those \npure of heart. \n\nAfter thanking him you return home and live happily ever after")
        elif choice=="right":
            print("\nThe bussines man offered you a guest bedroom so you can spend the night. \nAfter hearing some strange noise in the middle of the night you get up to investigate. \nYou open a creaking wooden door and find the bussines man covered in blood. \nYou try to run away but fail. The man turned out to be a vampire and he kills you because you discovered his secret.\n\nYou are dead. \nGAME OVER")
        else:
            print("ERROR! WRONG INPUT!")

elif first_choice=="left":
    print("\nUnfortunately you have made the worong choice. \n\nAs soon as you entered the forest you fell and hit your head against a very large rock. \nYou have now become a vengeful spirit who will roam this forest for ethernity!")

else:
    print("ERROR! WRONG INPUT!")