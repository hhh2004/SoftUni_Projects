employees = {}
while True:
    command = input()
    if command == "End":
        break
    command = command.split(' -> ')
    company = command[0]
    employee_id = command[1]
    if company in employees.keys():
        if employee_id in employees[company]:
            continue
        else:
            employees[company].append(employee_id)
    else:
        employees[company] = [employee_id]

for company in employees.keys():
    print(company)
    [print(f"-- {employee_id}") for employee_id in employees[company]]
