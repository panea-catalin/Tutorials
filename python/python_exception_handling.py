print('###Exceptions###\n')

print('###Common Exceptions\n')

# Exception (this is what almost all the others are built off of)
# AttributeError - Raised when an attribute reference or assignment fails.
# IOError - Raised when an I/O operation (such as a print statement, the built-in open() function or a method of a file object) fails for an I/O-related reason, e.g., “file not found” or “disk full”.
# ImportError - Raised when an import statement fails to find the module definition or when a from ... import fails to find a name that is to be imported.
# IndexError - Raised when a sequence subscript is out of range.
# KeyError - Raised when a mapping (dictionary) key is not found in the set of existing keys.
# KeyboardInterrupt - Raised when the user hits the interrupt key (normally Control-C or Delete).
# NameError - Raised when a local or global name is not found.
# OSError - Raised when a function returns a system-related error.
# SyntaxError - Raised when the parser encounters a syntax error.
# TypeError - Raised when an operation or function is applied to an object of inappropriate type. The associated value is a string giving details about the type mismatch.
# ValueError - Raised when a built-in operation or function receives an argument that has the right type but an inappropriate value, and the situation is not described by a more precise exception such as IndexError.
# ZeroDivisionError - Raised when the second argument of a division or modulo operation is zero.

print('###ZeroDivisionError###\n')
try:
    1 / 0
except ZeroDivisionError:
    print("can't divide by 0\n")

print('###Bare Excepts###\n')
try:
    1 / 0
except:
    print("can't divide by 0\n")

print('###KeyError###\n')
my_dict = {"a":1, "b":2, "c":3}
try:
    value = my_dict["d"]
except KeyError:
    print("that key doesn't exist\n")

print('###IndexError###\n')
my_list = [1, 2, 3, 4, 5]
try:
    my_list[6]
except IndexError:
    print("that index doesn't exist\n")

print('###Multiple Exceptions###\n')
my_dict = {"a":1, "b":2, "c":3}
try:
    value = my_dict["d"]
except IndexError:
    print("the index doesn't exist")
except KeyError:
    print("the key doesn't exist")
except:
    print("some other error occured")

try:
    value = my_dict["d"]
except(IndexError, KeyError):
    print("an index or a key error occured")

print('###The finally Statement###\n')
try:
    value = my_dict["d"]
except KeyError:
    print("a key error occured")
finally:
    print("the finally statement has executed")

print('###try, except, or else###\n')
try:
    value = my_dict["a"]
except KeyError:
    print("a key error occured")
else:
    print("no error occured")
finally:
    print("the finally statement ran")