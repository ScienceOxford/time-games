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
    display.clear()
    for item in sequence:
        if item == "A":
            music.play("")
        if item == "B":
            music.play("A")
        music.play("R")

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