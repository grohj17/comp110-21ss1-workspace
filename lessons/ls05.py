"""Relative reassignment."""
a: int = 3
b: str = "<"


b += str(a)
print(b)
b += str(a)
print(b)
b += str(a)
print(b)