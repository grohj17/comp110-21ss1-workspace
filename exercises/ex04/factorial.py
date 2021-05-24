"""An exercise in computing the factorial of an int."""

__author__ = "730201179"


number: int = int(input("Choose a number: "))
i: int = 1
fac: int = 1
while number >= i:
    fac = fac * i
    i = i + 1  
print("Factorial: " + str(fac))