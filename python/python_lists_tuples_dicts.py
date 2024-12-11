print('\t###Lists Tuples Dictionaries###\n')

print('###Lists###\n')

my_list = [1, 2, 3]
print(my_list)

my_second_list = list()
my_second_list = ["a", 1, "Python", 3]
print(my_second_list)

my_nested_list = [my_list, my_second_list]
print(my_nested_list)

print('\n###Combine Lists with the Extend Method###\n')
combo_list = []
one_list = [4, 5]
combo_list.extend(one_list)
print(combo_list)

print('\n###Add the two lists\n')
my_list = [1, 2, 3]
my_second_list = ["a", "b", "c"]
combo_list = my_list + my_second_list
print(combo_list)

print('\n###Sort List\n')
new_list = [32, 453, 34, 123, 54, 7]
new_list.sort()
print(new_list)

print('\n###Slice List\n')
print(new_list[0:3])

print('\n###Tuples###\n')
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[0:3])
another_tuple = tuple()
abc = tuple([1, 2, 3])
print(type(abc[0]))
abc_list = list(abc)
print(type(abc_list))

print('\n###Dictionaries###\n')
my_dict = {}
another_dict = dict()
my_other_dict = {"one":1, "two":2, "three":3}
print(my_other_dict)
print(my_other_dict['one'])
my_dict = {"name":"Mike", "address":"juve 52"}
print(my_dict["name"])
print(my_dict.keys())
print("name" in my_dict)