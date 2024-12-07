#Coin Flipping Simulator

#Ask the user if they want to flip the coin another time, each time
#And tally up the number of heads and tails

import random #To randomise the heads and tails

head,tail = 0,1
h=t=0 #Setting count of heads and tails as 0

print('Welcome to Coin Flipping Simulator!')
print('\nEach time, input Y or N for either continue the simulator or stop it.')

while True:
    input_ = input('Do you wish to flip a coin? (y/n) ')
    if input_ == 'y':
        r = random.randrange(2)
        if r == 0:
            print('The outcome was Heads!')
            h+=1
        else:
            print('The outcome was Tails!')
            t+=1
    elif input_ == 'n':
        print('Thank you for playing!')
        print('\nHere are the results:\nTotal no. of heads = ',h,'\nTotal no. of tails = ',t)
        break
    else:
        print('There seems to be a typo in your input. Why not try again?')
