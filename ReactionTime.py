import time
import random
import gpiozero
led = gpiozero.LED(26)
led.off()
while True:
    print("When The LED Lights Up (and the prompt tells you to), Press ENTER On Your Keyboard!\n")
    number = random.randint(2, 6)
    time.sleep(number)
    led.on()
    start = time.time()
    input("PRESS ENTER!!! ")
    end = time.time()
    led.off()
    reaction_time = end - start
    rounded = round(reaction_time, 5)
    input("It took you "+str(reaction_time)+"(About "+str(rounded)+" sec) seconds to respond! Press ENTER to play again! ")
    
