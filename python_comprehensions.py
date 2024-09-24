print('###Comprehensions###\n')

print('###List Comprehensions\n')

# x = [i for i in range(5)]
# print(x)

# x = ['1', '2', '3', '4', '5']
# y = [int(i) for i in x]
# print(y)

# x = [' asdf', ' asdf ', 'asdf ']
# trimmed = [s.strip() for s in x]
# print(trimmed)

# vec = [[1,2,3], [4,5,6], [7,8,9]]
# print(vec)
# new_vec = [num for elem in vec for num in elem]
# print(new_vec)

print('###Dictionary Comprehensions\n')

# print( {i: str(i) for i in range(5)} )

# my_dict = {1:"dog", 2:"cat", 3:"hamster"}
# print( {value:key for key, value in my_dict.items()} )

print('###Set Comprehensions\n')

my_list = [1, 2, 2, 3, 4, 5, 5, 7, 8]
# my_set = set(my_list)
# print(my_set)
my_set = {x for x in my_list}
print(my_set)