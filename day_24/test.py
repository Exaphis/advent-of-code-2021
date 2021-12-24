z = 0


def f(digit: int, shift_z: bool, x_inc: int, y_inc: int):
    # reverse-engineered blocks from input.txt
    # each block begins with "inp z" and ends with "add z y"
    # z acts like a stack of base 26 numbers
    global z

    # z % 26 gets the last item added to the stack
    x = (z % 26) + x_inc

    if shift_z:
        # remove the last item on the stack
        z //= 26

    if x != digit:
        # add new item to stack (new item will always be non-zero as digit is non-zero!)
        z *= 26

        # y_inc must be <= 16, otherwise the new number may not fit??
        # check this in the solver
        z += digit + y_inc
    else:
        # don't add a new item
        pass


# goal: list is empty at the end (z == 0)
# i.e. x == digit whenever possible so we do not add to the stack

# this is possible when x_inc < 10 (otherwise x must be >= 10 and x cannot equal digit)

# it happens to be the case that x_inc < 10 when shift_z is True
