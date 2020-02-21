from microbit import *
import random
import music

'''
------------WHAT DOES THE MICROBIT DO?------------
'''
sequence = []
options = ["A", "B", "C", "D", "E", "F"]
time = 500

def action():
    global sequence
    choice = random.choice(options)
    sequence.append(choice)
    display.clear()
    for item in sequence:
        music.play(item)
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
        if accelerometer.was_gesture("left"):
            response.append("C")
        if accelerometer.was_gesture("right"):
            response.append("D")
        if accelerometer.was_gesture("up"):
            response.append("E")
        if accelerometer.was_gesture("down"):
            response.append("F")

'''
------------WHAT HAPPENS AT THE END?------------
'''
score = 0

def correct():
    global time, score
    time -= 20
    score += 1
    display.show(Image.YES)

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
    print(sequence)
    reaction()
    if sequence == response:
        correct()
    else:
        incorrect()
        break
    sleep(1000)

display.scroll("GAME OVER")
sleep(100)
display.show(Image.NO)