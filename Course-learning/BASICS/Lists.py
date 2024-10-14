#lists => data structures which can hold different datatypes
#arrsy => data structures which can hold same datatypes
belts_colour = ["white", "blue", "Red"] #LIST
print (belts_colour)

#To print elements in LIST
for belt in belts_colour:    
    print(belt)

#Add element into LIST
belts_colour.append("orange")
print (belts_colour)

#Add elememt in particular place in a LIST
#In List element starts from 0,1,2,3
belts_colour.insert(1,"Pink")
print (belts_colour)

#To find the lenght of LIST
print(len(belts_colour))