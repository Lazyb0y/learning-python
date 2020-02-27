def hello_func():
    print('Hello Function!')


def hello_func_return():
    return 'Hello Function with Return!'


def hello_func_args(greeting):
    return '{} Function.'.format(greeting)


def hello_name(greeting, name='You'):
    return '{} {}.'.format(greeting, name)


hello_func()
print(hello_func_return())
print(hello_func_args('Hi Ema'))
print(hello_name('Hi'))
print(hello_name('Hi', 'Raihan'))

# Chain
print(hello_func_return().upper())


def student_info(*args, **kwargs):
    print(args)
    print(kwargs)


student_info('Math', 'Arts', name='Foysal', age=22)

courses = ['Math', 'Art']
info = {'name': 'Ahamed', 'age': 15}

student_info(*courses, **info)

# Number of days per month. First value placeholder for indexing purposes.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
    """Return True for leap years, False for non-leap years."""

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    """Return number of days in that month in that year."""

    if not 1 <= month <= 12:
        return 'Invalid Month'

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]


print(is_leap(2020))
print(days_in_month(2017, 2))
