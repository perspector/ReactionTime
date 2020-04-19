import time
import random

while True:
    print("When the prompt tells you to, press ENTER On Your Keyboard!\n")
    number = random.randint(2, 6)
    time.sleep(number)
    start = time.time()
    input("PRESS ENTER!!! ")
    end = time.time()
    reaction_time = end - start
    rounded = round(reaction_time, 5)
    input("It took you "+str(reaction_time)+"(About "+str(rounded)+" sec) seconds to respond! Press ENTER to play again! ")
    
