alphabets =["A", "B", "C"]

#for loop
for alpha in alphabets:
    print(alpha)
studentScores = []
twoScores = input("Enter total score of two subjects: ")
studentScores.append(twoScores)
total = sum(studentScores)
print(total)
sum = 0
for score in studentScores:
    sum +=score
print (sum)

#max
##way1 
print(max(studentScores))
##way2
max_score=0
for score in studentScores:
    if(max_score<score):
        max_score =score
print( max_score)           