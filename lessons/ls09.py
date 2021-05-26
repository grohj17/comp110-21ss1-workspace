"""An example function definition"""

def my_max(a: int, b: int) -> int:
    """Returns the largest parameter."""
    if a >= b:
        return a
    else:
        return b

my_max(5, 8)
