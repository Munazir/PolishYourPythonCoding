# 1. Reverse a given string using stack

given_string = "rizanuM si eman yM"
reversed_string = ""


# solution
import stack
stk = stack.Stack()

for char in given_string:
    stk.push(char)

while not stk.is_empty():
    reversed_string+=stk.pop()
print(reversed_string)
