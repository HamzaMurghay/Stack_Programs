# Postfix Evaluator Program

stack = []
top = -1
operations = ['^', '*', '/', '%', '+', '-']

expression = input("Enter the expression to evaluate: ")


for i in expression:
    print(stack)
    if i.isnumeric():
        stack.append(i)
    elif i in operations:
        op1 = stack.pop()
        op2 = stack.pop()
        if i == '^':
            i = "**"
        stack.append(str(eval(op2+i+op1)))

print(f"The value of expression is: {stack[top]}")


"""Rules:
   1)If input read from postfix expression is an operand, push operand to stack.
   2) If input read from postfix expression is an operator, pop the first 2 operand in stack and implement the expression using the following operations:

   op1 = STACK.pop()
   op2 = STACK.pop()
   result = op2 operator op1

   3)push the result of the evaluation to stack
   4)Repeat steps 1 to steps 3 until end of postfix expression

   Finally, at end of the operation, only one value will be left in the stack.The value is the result of postfix evaluation."""

