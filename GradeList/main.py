student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}


for name in student_scores:
    student_grades[name] = ""

for name in student_scores:
    if student_scores[name] <= 70:
        student_grades[name] = "Fail"
    elif student_scores[name] <= 80:
        student_grades[name] = "Acceptable"
    elif student_scores[name] <= 90:
        student_grades[name] = "Exceeds Expectations"
    elif student_scores[name] <= 100:
        student_grades[name] = "Outstanding"
print(student_scores)
print("")
  

print(student_grades)





