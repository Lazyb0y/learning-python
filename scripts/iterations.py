nums = [1, 2, 3, 4, 5]

# For Loop
for num in nums:
    print(num)

# Break
for num in nums:
    if num == 3:
        print('Found')
        break
    print(num)

# Continue
for num in nums:
    if num == 3:
        print('Found')
        continue
    print(num)

# Range
for i in range(1, 11):
    print(i)

# While Loop
x = 0

while x < 10:
    print(x)
    x += 1

# Infinite Loop
x = 0

while True:
    if x == 5:
        break
    print(x)
    x += 1
