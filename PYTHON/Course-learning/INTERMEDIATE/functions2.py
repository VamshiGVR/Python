# LAMBDA parameters:expression

#without lambda
def double(x):
    return x*2
print(double(10))

#Using Lambda
##Single parameter
double = lambda x:x*2
print(double(10))

##Two parameters
multiply = lambda x,y: x*y 
print(multiply(5,5))

##Three parameters
multiply = lambda x,y,z: x*y-y 
print(multiply(5,5,5))

##WithStrings
AddNames = lambda x,y: x + " "+ y 
print(AddNames("Bro","Code"))

##  ifelse
Check = lambda age:True if age>18 else False
print(Check(14))
print(Check(20))