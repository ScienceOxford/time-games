from microbit import *
import random
import music

'''
------------WHAT DOES THE MICROBIT DO?------------
'''
sequence = []
options = ["A", "B"]

def action():
    global sequence
    choice = random.choice(options)
    sequence.append(choice)

    for item in sequence:
        display.show(item)
        sleep(500)
        display.clear()
        sleep(500)

'''
------------WHAT SHOULD THE PLAYER DO?------------
'''
def reaction():
    global response, sequence
    response = []
    while 0 <= len(response) < len(sequence):

        if button_a.was_pressed():
            response.append("A")
        if button_b.was_pressed():
            response.append("B")

'''
------------WHAT HAPPENS AT THE END?------------
'''
def correct():
    display.show(Image.YES)

def incorrect():
    global sequence
    sequence = []
    display.show(Image.NO)

'''
------------THE MAIN GAME CODE------------
'''
while True:
    action()
    reaction()
    if sequence == response:
        correct()
    else:
        incorrect()
    sleep(1000)

# STEP 0 = microbit images + doc comments
# STEP 1 = play the game - what is happening? think about improvements you might want to make
# STEP 2 = talk through the main game code - what is happening
# STEP 3 = get improvement ideas ONE AT A TIME - which section of code would you need to edit?
# STEP 4 = introduce extension ideas / worksheets
    # edit ending - want the game to end? break + end game sequence; want to keep score? variable;
    # edit micro:bit - sounds instead of letters? speaker + import music/speech; extra responses? edit options;
        # get quicker? variable + edit sleep time;
    # edit player - gestures instead of buttons? accelerometer; extra responses? add to if statement;
        # add joystick for extra buttons? add joystick functions;
