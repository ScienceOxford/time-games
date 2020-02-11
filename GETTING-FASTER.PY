from microbit import *
import random

'''
------------WHAT DOES THE MICROBIT DO?------------
'''
sequence = []
options = ["A", "B"]
time = 500

def action():
    global sequence
    choice = random.choice(options)
    sequence.append(choice)
    
    for item in sequence:
        display.show(item)
        sleep(time)
        display.clear()
        sleep(time)

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
    global time
    time -= 20
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