courses = {}
while True:
    command = input()
    if command == "end":
        break
    command = command.split(' : ')
    course_name = command[0]
    student_name = command[1]
    if course_name in courses.keys():
        courses[course_name].append(student_name)
    else:
        courses[course_name] = [student_name]

for course_name in courses.keys():
    print(f"{course_name}: {len(courses[course_name])}")
    for student_name in courses[course_name]:
        print(f"-- {student_name}")
