import math


def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    return x/y

def pow(x,y):
    return x**y

def sqrt(x):
    return math.sqrt(x)

print("Addition: 4+5=",add(4,5))
print("Subtraction: 4-5=",sub(4,5))
print("Multiplication: 4*5=",mul(4,5))
print("Division: 4/5=",div(4,5))
print("Exponentiation: 4^5=",pow(4,5))
print("Square root: sqrt(4)=",sqrt(4))