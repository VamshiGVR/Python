## LAMBDA
x = lambda a: a+10

z = lambda a,b : a*b
print(z(5,5))

def myfunc(a,b):
    return a-b
print(myfunc(5,2))

def ldfunc(n):
    return lambda a:a*n
mydouble = ldfunc(2)
print(mydouble(12))

def ldfunc(a, n):
    return a*n
print(ldfunc(15,2))
