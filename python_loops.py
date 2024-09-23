print('###The for Loop###\n')

my_list = list(range(5))

print(my_list)
print('###')
my_other_list = list(range(1, 10, 2))
print(my_other_list)
print('###')
for number in my_list:
    print(number)
print('###')
i = 0

while i < 10:
    if i == 3:
        i += 1
        continue

    print(i)

    if i == 5:
        break
    i += 1

print('###')
my_list = list(range(5))

print(my_list)

for i in my_list:
    if i == 3:
        print("3 is in the list")
        break
    print(i)
else:
    print("item not found in the list")