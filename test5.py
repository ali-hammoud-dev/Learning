def calculate_average_grade(students_list):
    total_sum = 0
    total_count = 0

    for student in students_list:
        grades = student['grades']
        total_sum += sum(grades)
        total_count += len(grades)

    average_grade = total_sum / total_count
    return average_grade

# Example list of students
students_list = [
    {
        'name': 'Jose',
        'school': 'Computing',
        'grades': (66, 77, 88)
    },
    {
        'name': 'Emma',
        'school': 'Engineering',
        'grades': (75, 82, 91)
    },
    {
        'name': 'Michael',
        'school': 'Mathematics',
        'grades': (88, 91, 78)
    }
]

# Calculate and print the average grade using the function
average_grade = calculate_average_grade(students_list)
print(f"Average Grade for the Entire Class: {average_grade:.2f}")
