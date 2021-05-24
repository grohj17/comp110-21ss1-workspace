"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730201179"

from random import randint

print("Your fortune cookie says...")
some_int: int = randint(0,3)
if some_int == 0:
    print("A faithful friend is a strong defense.")
else:
    if some_int == 1:
        print("A feather in the hand is better than a bird in the air.")
    else:
            if some_int == 2:
                print("A fresh start will put you on your way.")
            else:
                if some_int == 3:
                    print("A friend asks only for your time not your money.")
print("Now, go spread positive vibes!")