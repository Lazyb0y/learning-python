student = {'name': "John", 'age': 25, 'courses': ['Math', 'CompSci']}

# Add / Update
print(student)
print(student['courses'])

print(student.get('name'))
print(student.get('phone'))
print(student.get('phone', 'Not Found'))

student['phone'] = '01783-902751'
print(student.get('phone'))

student.update({'name': 'Foysal', 'age': 28, 'blood_group': 'B+'})
print(student)

# Delete
del student['phone']
print(student)

age = student.pop('age')
print(age)

# Loop
print(student.keys())
print(student.values())
print(student.items())

for key, value in student.items():
    print(key, value)
