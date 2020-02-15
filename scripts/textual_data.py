message = "Ahamed's World"
print(message)

print(message[0:6])

# Multi line
multi_line_message = """This is a
multi line message"""
print(multi_line_message)

print("Length: " + (len(multi_line_message)).__str__())

# String method(d)
print(message.lower())
print(message.count('am'))
print(message.find('am'))

new_message = message.replace('World', "Universe")
print(new_message)

name = "Ahamed"
message = "Hello, {}. Welcome!".format(name)
print(message)

message = f"Hello, {name.upper()}. Welcome again!"
print(message)

# Helping methods
print(dir(message))
print(help(str))
