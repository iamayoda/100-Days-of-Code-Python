student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

#BUILT-IN FUNCTIONS

#1.1 SUM
total_exam_scores = sum(student_scores)
print(total_exam_scores)

#1.2. MANUAL ADDING
sum = 0

for score in student_scores:
    sum += score
print(sum)


#2.1 MAX
print(max(student_scores))

#2.2 MANUALLY FINDING MAXIMUM NUMBER
for score in student_scores:
    asc_order = sorted(student_scores)
print(asc_order[-1])

#Alternaive
max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score

print(max_score)
