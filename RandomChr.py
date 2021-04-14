import random
stop = ''
import os
while stop != 'q':
    os.system('cls')
    num = random.choice(range(1,3000))
    print(chr(num))
    stop = input('Press enter to generate another character.'
    + ' Input "q" to quit.')
