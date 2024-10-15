#lists => data structures which can hold different datatypes
#arrsys => data structures which can hold same datatypes
colors = ["white", "blue", "Red", "Ash"] #LIST
print (colors)

#To print elements in LIST
for color in colors:    
    print(color)

#Add element into LIST
colors.append("orange")
print (colors)

#Add elememt in particular place in a LIST
#In List element starts from 0,1,2,3
colors.insert(1,"Pink")
print (colors)

#To find the lenght of LIST
print(len(colors))


#Print single element
print(colors[3])


#Replace directly in list 
colors[0] ="White"
print(colors)

#Adding directly to list
colors.append("Black")
print(colors)

#Removing directly to list
colors.remove("Ash")
print(colors)


#removing directly from list with its index
colors.pop(3)
print(colors)

#clear list
colors.clear()
print(colors)