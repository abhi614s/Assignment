'''
Write a program to construct a dictionary from the two lists containing the names of students and their corresponding subjects. The dictionary should map the students with their respective subjects. Let’s see how to do this using for loops and dictionary comprehension.

'''

students = ["Alice", "Bob", "Charlie"]
subjects = ["Math", "Science", "English"]

student_subjects_dict = {}

for i in range(len(students)):
    student_subjects_dict[students[i]] = subjects[i]

print(student_subjects_dict)
