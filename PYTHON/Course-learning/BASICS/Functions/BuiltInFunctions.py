#function is always followed by ()parathesis
name ="Python"

age = 1

    #Lists
Cars=["BMW", "NISSAN", "HONDA"]

rng = range(0, 10) #range(startValue, endValue) #but doesnt includes EndValue
rng = range(0, 20, 2) #range(startValue, endValue, incrementValue) #but doesnt includes EndValue
    #range(10,-10,2)

    #Dict
employes = [{"name": "PM","Salary": 30}, {"name": "DO","Salary": 20},{"name":"PO","Salary":10}]

    #print function
    #/n  for next line
print("my name is",name,"i m",age,"years old")
print("my name is ", name, "i m", age, "years old", sep="/")

    #help = get the documentation of function passed into it
    #Work for custom functions also
#help(print)

    #Range
    #for -ve also
print(rng)
    #To print values
numberList=(list(rng))
print(numberList)
    
    #len
num_char = len(name)
print("Charecter in letter: ", num_char)

    #Maps: Maps a custom or inbuilt functions into give List etc
    #EX:1
lengths =map(len, Cars)
print(list(lengths))
    #EX2
lengths =map(lambda x:x+"s", Cars) #x:x+"s" takes each element from List and add s at end
print(list(lengths))
    
    #Filter : takes a elements from list pass it to funcitons, if it is true then keeps it and if not removes it

    #METHOD1
    #CustomFunction
def verifyLenght(string):
    return len(string)>4
filtered = filter(verifyLenght, Cars)
print(list(filtered))
    #METHOD
    #USING LAMBDA FUNCTIONS
filtered = filter(lambda x:len(x)>4, Cars)
print(list(filtered))

    #SUM #can pass list, tuples, sets which contains numbers int, float
    #used range from above 
print(sum(numberList))
print(sum(numberList, start =100))  #here start=100 is starter value #can be negitive also

    #SORTED :sort in ascending order or desending order
sortedNumbers = sorted(numberList, reverse = True)#sorted as reverse
print(sortedNumbers)

    #Sorted based on key word
sortedEmployes = sorted(employes, key= lambda employee: employee["Salary"])
    #Sorted based on key word in revese order
sortedEmployesReverse = sorted(employes, key= lambda employee: employee["Salary"], reverse=True)
print("ORDER: ",sortedEmployes)
print("ORDER: ",sortedEmployesReverse)

    #enumertate
print("ENUMERATE")
for index, car in enumerate(Cars):
    print(f"{index+1}.{car}")

    #open
    #Method1
file = open("builtinfunctioncreated1.txt", "w") #w stands for createfile
file.write("hello\nThis created by first builtin function")# write is used to write in file
file.close()#to close file
    #Method2
with open("builtinfunctioncreated2.txt", "w") as file:
    file.write("hello\nThis created by second builtin function")

with open("builtinfunctioncreated2.txt", "r") as file:#r is used to read inside file
    text = file.read()
    print(text)

with open("builtinfunctioncreated1.txt", "a") as file: #a is used to append at end of file #not for replacing content
    file.write("\ncreated this line by append")

    # we have more modes like a, r, w, ar,etc./.....          