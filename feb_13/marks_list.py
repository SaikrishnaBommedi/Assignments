no_of_students = int(input())
marks_list = {}
for i in range(no_of_students):
    name = input("Enter student name: ")
    percentage = int(input("Enter percentage: "))
    marks_list[name] = percentage


for student in marks_list:
    print(student, str(marks_list[student])+"%")