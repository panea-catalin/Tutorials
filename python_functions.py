print('###Functions###\n')
print('###Defining###\n')
def function():
    pass

print('\n###Example of a function###\n')
def add(a,b):
    return a+b
total = add(1,2)
print(total)

total2 = add(a=1,b=3)
print(total2)

print('\n###Keyword Arguments###\n')
def adding(c, a=2, b=3):
    return a+b+c

total3 = adding(1, a=4, b=5)
print(total3)

total4 = adding(1)
print(total4)

print('\n###*Args and **KWArgs###\n')
def many(*args, **kwargs):
    print(args)
    print(kwargs)
many(1,2,3, name="Gman", job="stay at home astronaut")

print('\n###Scope and Globals###\n')
def func_a():
    global a
    a = 1
    b = 2
    return a+b

def func_b():
    c = 3
    return a+c

print( func_a() )
print( func_b() )