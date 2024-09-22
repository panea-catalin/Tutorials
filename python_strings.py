print('\t###Strings###\n')

print('###Defining Strings\n')
my_string = "Welcome to Python!\n"
print('I defined: my_string = "Welcome to Python!"')
print(my_string)
print('###\n')

another_string = 'She sells sea shells on the sea shore.\n'
print("I defined another string: 'She sells sea shells on the sea shore.'")
print(another_string)
print('###\n')

long_string = '''This is 
a multi line
string\n'''
print("And a multi line string: '''This is a multi line string'''")
print(long_string)

print('###Type and Type Casting\n')
my_number = 123
print('I defined "my_number = 123" and casted it as a string "my_string = str(my_number)"\n')
my_string = str(my_number)
print('Printing them "print(type(my_string),type(my_number))" yields:\n')
print(type(my_string),type(my_number),'\n')

print('###String ID\'s###\n')
print('''my_string = 'abc'
print('This is the id of "my_string" : ' + str(id(my_string)))
print('This is the value of "my_string" : ' + my_string)
my_string = 'cba'
print('This is the id of "my_string" after i changed the value : ' + str(id(my_string)))
print('This is the value of "my_string" : ' + my_string)
''')
my_string = 'abc'
print('This is the id of "my_string" : ' + str(id(my_string)))
print('This is the value of "my_string" : ' + my_string)

my_string = 'cba'
print('This is the id of "my_string" after i changed the value : ' + str(id(my_string)))
print('This is the value of "my_string" : ' + my_string)

print('\n###String Concatenation\n')
print('''string_one = "some"
string_two = "choco"
concatenated_string = string_one + string_two
print(concatenated_string)
''')
string_one = "some"
string_two = "choco"
concatenated_string = string_one + string_two
print("This is the concatenated string: " + concatenated_string)

print('\n###String Methods###\n')
print('''print(my_string.upper())
print(my_string.capitalize())
''')
print("This is the string after using .upper: " + my_string.upper())
print("This is the string after using .capitalize: " + my_string.capitalize())

print('\n###String Slicing###\n')
print('''some_string = 'The word "python" refers to a snek.'
print(some_string[0:-5])
print(some_string[0:3])''')
some_string = 'The word "python" refers to a snek.\n'
print("This starts dispaying from 0 to -5: " + some_string[0:-5])
print("This starts dispaying from 0 to 3: " + some_string[0:3])

print('\n###String Formatting###')