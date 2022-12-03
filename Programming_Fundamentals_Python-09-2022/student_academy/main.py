grades = {}
num_records = int(input())
for _ in range(num_records):
    student_name = input()
    grade = float(input())
    if student_name in grades.keys():
        grades[student_name].append(grade)
    else:
        grades[student_name] = [grade]
for student_name in grades.keys():
    average_grade = sum(grades[student_name])/len(grades[student_name])
    if average_grade >= 4.5:
        print(f"{student_name} -> {average_grade:.2f}")
