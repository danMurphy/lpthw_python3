def add(a, b):
    print(f"Adding {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"Subtracting {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"Multiply {a} * {b}")
    return a * b

def divide(a, b):
    print(f"Divide {a} / {b}")
    return a / b

print("let's do some math with just functions!")

age = add(40, 2)
height = subtract(78, 5)
weight = multiply(90, 2)
iq = divide(100, 45)

print(f"Age : {age} Height : {height} weight : {weight} iq : {iq}")

# A puzzle for the extra credit, type it in anyway
print("Heres the puzzle")

what =  add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes : ", what, "Can you do it by hand")