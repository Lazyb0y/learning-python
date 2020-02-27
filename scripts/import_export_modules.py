import my_module as mm
import sys
import random

# Import selected element only
# from my_module import find_index
# from my_module import find_index, test
# from my_module import find_index as fi, test
# from my_module import *
# index = fi(courses, 'Math')

courses = ['History', 'Math', 'Physics', 'CompSci']

index = mm.find_index(courses, 'Math')
print(index)

print(sys.path)

random_course = random.choice(courses)
print(random_course)
