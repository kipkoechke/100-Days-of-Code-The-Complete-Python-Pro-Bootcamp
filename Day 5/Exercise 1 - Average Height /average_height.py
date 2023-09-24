student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
   # Convert each element to an integer
    student_heights[n] = int(student_heights[n])  # type: ignore

total_height = 0
for height in student_heights:
    total_height += height  # type: ignore
print(f"total height = {total_height}")

number_of_students = 0
for student in student_heights:
    number_of_students += 1
print(f"number of students = {number_of_students}")

average_height = round(total_height / number_of_students)
print(f"average height = {average_height}")
