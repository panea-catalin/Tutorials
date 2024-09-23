# print('###The If Statement###\n')

# var1 = 1
# var2 = 3
# if var1 > var2:
#     print('This is True.')
# else:
#     print('Not True!')

# print('')

# # print('###Using Input###\n')
# # value = input("What's your age? \n")
# # value = int(value)

# # if value > 18 or value == 18:
# #     print('Congrats, you can apply for a driver permit')
# # elif value < 18 and value > 0:
# #     print("Sorry, too young to drive.")
# # else:
# #     print('I have no idea what happened!')

# print('###\n')

# my_list = [1, 2, 3, 4]
# x = 10
# # if x not in my_list:
# #     print("'x' is not in the list, so this is True!")

# # if x != 11:
# #     print("x is not eq to 11!")
# z = 12
# if x not in my_list and z != 11:
#     print("True")

empty_list = []
empty_tuple = ()
empty_string = ""
nothing = None

if empty_list == []:
    print("Empty list!")
else:
    print("Not Empty!")

if empty_tuple:
    print("Not empty!")
else:
    print("empty")
empty_string = " 123 "
if not empty_string:
    print("True, so empty!")

if empty_string == "":
    print("True, so empty!")

if not nothing:
    print("Then it's nothing!")