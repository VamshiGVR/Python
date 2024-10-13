alphabets =["A", "B", "C"]

#for loop
for alpha in alphabets:
    print(alpha)
student_scores = [100, 150, 144, 141, 213, 94, 104, 154, 124, 194 ]
total = sum(student_scores)
print(total)
sum = 0
for score in student_scores:
    sum +=score
print (sum)

#max
##way1 
print(max(student_scores))
##way2
max_score=0
for score in student_scores:
    if(max_score<score):
        max_score =score
print( max_score)