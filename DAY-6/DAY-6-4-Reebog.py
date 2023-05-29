# CODE FOR https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()
def turn_around():
    turn_left()
    turn_left()
def jump():
    
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
counter = 0
while at_goal() != True:
    if front_is_clear():
        move()
    else:
        turn_left()
        while wall_on_right() == True:
            counter = counter + 1
            move()
        turn_right()
        move()
        turn_right()
        while counter > 0:
            counter=counter-1
            move()
        turn_left()

  

