#we can add or remove elements, but cant replace as they are unordered,  no duplicates
colors = {"white", "blue", "Red", "Ash"} #SETS
print (colors)

#add
#wont allow duplicates
colors.add("orange")
print(colors)

#add
colors.remove("Ash")
print(colors)

if "apple" in colors:
    print("found")
if "Red" in colors:
    print("found")
else:
    print("Not found")


color = input("What color are you looking for: ")

if color in colors: #case need to match
    print("found")
else:
    print("not found")