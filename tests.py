'''
# Stack implementation in python


# Creating a stack
def create_stack():
    stack = []
    return stack


# Creating an empty stack
def check_empty(stack):
    return len(stack) == 0


# Adding items into the stack
def push(stack, item):
    stack.append(item)
    print("pushed item: " + item)


# Removing an element from the stack
def pop(stack):
    if (check_empty(stack)):
        return "stack is empty"

    return stack.pop()


stack = create_stack()
push(stack, str(1))
push(stack, str(2))
push(stack, str(3))
push(stack, str(4))
print("popped item: " + pop(stack))
print("stack after popping an element: " + str(stack))


def checkprime(n):
    if n==1 or n==0:
        return 0
    for l in range(2,n//2):
        if n%l==0:
            return 0
    return 1


def getprime(num):
    if num%2==0:
        num = num+1

    while not checkprime(num):
        num = num+2
    return num

print(getprime(79793))
'''

someli = [1,2,3,4,5]

someli.append(someli.pop(someli[3]))
print(someli)
