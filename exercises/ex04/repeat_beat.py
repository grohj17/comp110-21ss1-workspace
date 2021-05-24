"""Repeating a beat in a loop."""

__author__ = "730201179"


beat: str = input("What beat do you want to repeat? ")
repetition: int = int(input("How many times do you want to repeat it? "))
i: int = 0
x: str = " "
if repetition <= 0:
    print("No beat...")
else:
    while i <= repetition:
        if i <= 0:
            x = beat
            i = i + 1
        else:
            x = x + " " + beat
        i = i + 1
    print(x)
