# Menu Driven Stack Operations Program:

stack = []
top = -1
max_s = int(input("Enter the maximum size of stack:"))


def push():
    global top
    e = int(input("Enter the element you wish to append:"))
    if top == max_s - 1:
        print("Overflow Error!")
        return 0
    stack.append(e)
    top += 1


def pop():
    global top
    if top == -1:
        print("Underflow Error!")
    e = stack.pop()
    top -= 1
    print(f"Popped element is {e}")


def peek():
    global top
    if top == -1:
        print("Stack is empty!")
        return 0
    print(f"The top element is {stack[top]}")


def search():
    global top
    e = int(input("Enter element to search:"))
    for i in range(0, top + 1):
        if stack[i] == e:
            print("Element found!")
            return 1
    print("Element not found!")


def menu():
    choice = 0
    try:
        while choice != 5:
            print("Enter the operation you wish to perform on stack:")
            print("1)Append an element")
            print("2)Pop an element")
            print("3)Peek at top")
            print("4)Search an element")
            print("5)End the Program")
            choice = int(input(""))
            if choice == 1:
                push()
            elif choice == 2:
                pop()
            elif choice == 3:
                peek()
            elif choice == 4:
                search()
            elif choice == 5:
                print("Thank you for using the program!")
            else:
                print("Invalid Choice!Please enter a valid option")
            print("")
    except:
        print("Error! Please try again\n")
        menu()


print("-------------------------------MENU-------------------------------")
menu()
