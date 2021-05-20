"""Allows the user to input two numerical variables that the program then uses in a series of numerical operators."""

__author__: str = "730201179"

left_input: str = input("Enter your first numerical variable. ")
right_input: str = input("Enter your second numerical variable. ")
left_integer: int = int(left_input)
right_integer: int = int(right_input)
print("Left-hand side: " + left_input)
print("Right-hand side: " + right_input)
exponentiation: int = left_integer ** right_integer
print(left_input + " ** " + right_input + " is " + str(exponentiation))
division: float = left_integer / right_integer
print(left_input + " / " + right_input + " is " + str(division))
integer_division: int = left_integer // right_integer
print(left_input + " // " + right_input + " is " + str(integer_division))
remainder: int = left_integer % right_integer
print(left_input + " % " + right_input + " is " + str(remainder))