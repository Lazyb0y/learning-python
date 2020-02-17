# Comparisons:
# # Equal:            ==
# # Not Equal:        !=
# # Greater Than:     >
# # Less Than:        <
# # Greater or Equal: >=
# # Less or Equal:    <=
# # Object Identity:  is
#
#
# # False Values:
#     # False
#     # None
#     # Zero of any numeric type
#     # Any empty sequence. For example, '', (), [].
#     # Any empty mapping. For example, {}.


if True:
    print('Condition was true')

language = 'Python'

if language == 'Python':
    print('Language: Python')
elif language == 'Java':
    print('Language: Java')
else:
    print('Unknown language')


condition = 'Test'

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in:
    print('Admin Page')
else:
    print('Bad Credentials')

if user == 'Admin' or logged_in:
    print('Admin Page')
else:
    print('Bad Credentials')

if not logged_in:
    print('Please Log In')
else:
    print('Welcome')


condition = None

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

a = [1, 2, 3]
b = [1, 2, 3]

print(id(a))
print(id(b))

print(a == b)
print(a is b)

b = a

print(a == b)
print(a is b)
