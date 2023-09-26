class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

# Define a function to use as the sorting key
def sorting_key(student):
    return (student.cgpa, student.name, student.roll_number)

# Example usage:
students = [
    Student("Ajay", "A001", 3.7),
    Student("boobie", "B002", 3.4),
    Student("charlie", "C003", 3.8),
]

# Sort the students using the custom sorting key
sorted_students = sorted(students, key=sorting_key, reverse=True)

# Print the sorted students
for student in sorted_students:
    print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")
