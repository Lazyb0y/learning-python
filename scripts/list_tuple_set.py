# List
courses = ['History', 'Math', 'Physics', 'CompSci']

print(courses)
print(len(courses))

print(courses[1])
print(courses[-1])
print(courses[0:2])

courses.append('Art')
courses.insert(0, 'English')
print(courses)

extended_course = ['Biology', 'Chemistry']
courses.extend(extended_course)
print(courses)

courses.remove('Math')
print(courses)

popped = courses.pop()
print(popped)
print(courses)

courses.reverse()
print(courses)

courses.sort()
print(courses)

nums = [1, 5, 2, 4, 3]

nums.sort(reverse=True)
print(nums)

nums.sort()
print(nums)

print(min(nums))
print(max(nums))
print(sum(nums))

print(courses.index('History'))
print('Art' in courses)
print('Math' in courses)

for course in courses:
    print(course)

for index, course in enumerate(courses):
    print(index, course)

for index, course in enumerate(courses, start=1):
    print(index, course)

courses_str = ', '.join(courses)
print(courses_str)

print(courses_str.split(', '))

# Tuple


# Mutable
list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1

print(list_1)
print(list_2)

list_1[0] = 'Art'

print(list_1)
print(list_2)

# Immutable
tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

# tuple_1[0] = 'Art'

print(tuple_1)
print(tuple_2)

# Sets
cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Math', 'Art', 'Design'}

print(cs_courses)

print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))
print(cs_courses.union(art_courses))


# Empty Lists
empty_list = []
empty_list = list()

# Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

# Empty Sets
empty_set = {}  # This isn't right! It's a dict
empty_set = set()
