import sys
print('''The first chapter in this section will give you a quick tutorial into Python’s 
    introspection abilities; basically you’ll learn how to make Python tell you about itself,
    which sounds kind of weird but is really quite valuable to know about. Next we’ll learn
    how to use ConfigParser, a neat little module that let’s you read and write config files. 
    After that we’ll take a look at logging. The os module can do lots of fun things, but we’ll 
    try to focus on the ones that I think you’ll find most useful. The subprocess allows you to 
    open other processes.

    You will find the sys module allows you to exit a program, get the Python path, acquire version 
    information, redirect stdout and a whole lot more. The thread module allows you to create threads
    in your program. We won’t dive too deep into that subject as it can get confusing pretty quickly.
    The time and datetime modules allow you to manipulate dates and time in Python, which has many
    applications when it comes to developing programs.''')

print('\n###The Python Type###\n')
x = "test"
y = 7
z = None

print(type(x))
print(type(y))
print(type(z))
print('\n###Dir###\n')
print(dir(sys))
print('\n###Help###\n')
help()