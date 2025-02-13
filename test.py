import math

history=[]

def add_to_history(operation, result):
    history.append(f"{operation} = {result}")

def add(a, b):
    result = a + b
    add_to_history(f"{a} + {b}", result)
    return result

def sub(a, b):
    result = a - b
    add_to_history(f"{a} - {b}", result)
    return result

def mul(a, b):
    result = a * b
    add_to_history(f"{a} * {b}", result)
    return result

def div(a, b):
    if b == 0:
        result = "Error: Division by zero"
    else:
        result = a / b
    add_to_history(f"{a} / {b}", result)
    return result

def pow(a,b):
    result=a**b
    add_to_history(f"{a}^{b}", result)
    return result

def sqrt(a):
    result=math.sqrt(a)
    add_to_history(f"Square root of {a}", result)
    return result

def clear_history():
    history.clear()


print("Addition: 4+5=",add(4,5))
print("Subtraction: 4-5=",sub(4,5))
print("Multiplication: 4*5=",mul(4,5))
print("Division: 4/5=",div(4,5))
print("Exponentiation: 4^5=",pow(4,5))
print("Square root: sqrt(4)=",sqrt(4))
print("All operations: ",history)