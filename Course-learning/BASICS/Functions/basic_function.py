#function is always followed by ()parathesis

#declaring function 
def greet(name):
    print(f"Hi {name}")
def greet(name, age):
    print(f"Hi {name}, you are age is {age}")

#calling function & passing arguments
greet("abc", 22)
greet("def", 12)


#Return values
def add(a,b):
    adding = a + b
    return adding

print(add(1,2))