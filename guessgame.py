
binary=False                    # set this to True or False
lonum,hinum=1,200               # range for the number

import random as r

the_num=r.randint(lonum,hinum)  # smart enough computer chooses a number randomly
print("I'm thinking of a number between",lonum,"and",hinum)

lo=1
hi=hinum
guesses=0

for i in range(lonum,hinum):    # repeat until guess is correct:

    guess=int(input ("What is your guess: "))
    if binary:  guess=lo+(hi-lo)//2
    else:       guess=r.randint(lo,hi)
    print("Guess:",guess)
    guesses=guesses + 1                      # increasing number of guesses
                                    # check if you are right!
    if guess > the_num:
        print("Lower!")
        hi=guess
    elif guess < the_num:
        print("Higher!")
        lo=guess
    else: break

print("That actually took",guesses,"guesses")
