# 1. Reverse a given string using stack

given_string = "rizanuM si eman yM"
reversed_string = ""

# solution
import stack

stk = stack.Stack()

for char in given_string:
    stk.push(char)

while not stk.is_empty():
    reversed_string += stk.pop()
print(reversed_string)

# 2. Check if an expression is balanced or not
# {[{}{}]}[()], {{}
# {}}, []
# {}()
# are
# balanced
# expressions.
#
# {()}[), {(})
# are
# not balanced.

# for this problem we are taking empty stack of characters
from collections import deque


def is_balanced(exp):
    if not exp or len(exp) % 2 != 0:
        return False

    # create a stack
    s = deque()
    for char in exp:

        if char == '[' or char == '{' or char == '(':
            s.append(char)

        if char ==


