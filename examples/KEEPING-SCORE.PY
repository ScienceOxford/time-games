from microbit import *
import random

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
score = 0

def correct():
    global score
    display.show(Image.YES)
    score += 1

def incorrect():
    global sequence, score
    sequence = []
    display.scroll(score)
    sleep(500)
    score = 0

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