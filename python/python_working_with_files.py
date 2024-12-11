print('###Working with files###\n')
print('###How to open a file###\n')

try:
    handle = open("test.txt")
except IOError:
    print("the file doesn't exist")
else:
    print("file opened")

print('###How to read a file###\n')
data = handle.read()
print(data)
handle.close()

print('###How to read one line###\n')
try:
    handle = open("test.txt")
except IOError:
    print("the file doesn't exist")
else:
    print("file opened")
try:
    data = handle.readline()
    print(data)
except IOError:
    print("the file is closed")
finally:
    handle.close()
print('\n###\n')
handle = open("test.txt", "r")
data = handle.readlines()
print(data)
handle.close()
print('\n###\n')
handle = open("test.txt", "r")
for line in handle:
    print(line)

handle.close()
print('\n###\n')
handle = open("test.txt","r")

while True:
    data = handle.read(1024)
    print(data)
    if not data:
        break

print('\n###Read binary files###')
try:
    handle.open("test.pdf", "rb")
except:
    print("file does not exist")
finally:
    handle.close()

print('\n###Writing files###')
handle = open("test.txt", "w")
handle.write("this is a test!")
handle.close()

print('\n###The with Operator###\n')
with open("test.txt") as file_handler:
    for line in file_handler:
        print(line)

try:
    with open("test.txt") as file_handler:
        for line in file_handler:
            print(line)
except IOError:
    print("IO error occured")
    