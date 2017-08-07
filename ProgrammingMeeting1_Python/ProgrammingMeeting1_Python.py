from Example import Example
from ExtendedExample import ExtendedExample

example = Example(10)

extended = ExtendedExample(10)

print(extended.value)
print(example)
print(extended)

list = [0]

for x in range(0, 10):
    list.append(Example(x))

for x in range(len(list)):
    print(list[x])

name = input("Enter your name:\n")

print("Hello %s! " % name)

age = int(input("How old are you?\n"))

print("You are %i years old!" % age)