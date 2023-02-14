# INFIX TO POSTFIX PROGRAM:

stack = []
top = -1
operations = ['(', ')', '^', '*', '/', '%', '+', '-']
assoc = ['+-', '-+', '*/', '*%', '/*', '/%', '%*', '%/']

expression = input("Enter the expression to convert: ")
postfix = ""


def push(e):
    global top
    stack.append(e)
    top += 1


def pop():
    global top
    stack.pop()
    top -= 1


def search(e):
    global top
    for k in range(0, 8):  # len(operations) = 8
        if operations[k] == e:
            return k


def precedence_checker(t, o):
    global postfix
    if t+o in assoc:
        postfix += stack[top]
        pop()
        if top == -1:
            push(o)
            return 1
        precedence_checker(stack[top], o)

    elif search(t) <= search(o) and t != '(':
        postfix += stack[top]
        pop()
        if top == -1:
            push(o)
            return 1
        precedence_checker(stack[top], o)
    else:
        push(o)


for i in expression:
    j = top
    if i.isalpha() or i.isnumeric():
        postfix += i

    elif i in operations:
        if top == -1:
            push(i)
        elif i == '(':
            push(i)
        elif i == ')':
            while j >= 0 and stack[j] != '(':
                postfix += stack[j]
                pop()
                j -= 1
            pop()

        else:
            precedence_checker(stack[top], i)

for i in range(top, -1, -1):
    postfix += stack[top]
    pop()

print(f"\nThe Postfix Expression is: {postfix}")


"""Rules For Infix to PostFix:
   1)Scan the Expression from left to right
   2)If element is operand then print Operand in postfix as it arrives
   3)If symbol is "(" push it on stack
   4)If symbol is ")" then pop all the elements from stack and print to postfix string till "(" appears the discard
     from stack
   5)If symbol Operator arrives and stack is empty then push this operator onto the stack
            i)If incoming Operator has Higher precedence than TOP of the stack operator then push this operator onto
              the stack

            ii)if incoming operator has lower or equal precedence than top of the stack then pop this 
               operator(the top of stack) and print in postfix array [unless it is '(', in that case just push incoming
               operator onto the top of stack].Then test the precedence of incoming operator with new top of the stack.
   6)At the end of the expression, pop and print all element of stack in postfix array."""

# Paste the following code(keeping the indentation) under elif of ')' to see the error I could not resolve (replace current code):
# for j in range(top, -1, -1):
#     while stack[j] != '(':
#         postfix += stack[j]
#         pop()
# pop()

# Also, in the if statement "elif search(t) <= search(o) and t != '(':" it doesnt account for operators with same
# precedence, that's why there's that long if statement at start. If you know a better and simpler way to do that
# hit me up

"""Test Examples:
   
   1) a+b
   2) (a+b)*c
   3) a+b*c-d/e
   4) (a+b-c)*d-(e+f)
   5) A-(B/C+(D%E*F)/G)*H
   6) a^b*(c-d)/(p-r)
   7) a+b-c*(d-(e/f))+g
   8) 2*7-18+6
   9) 6-(2+3)*3+8/2+3"""
