my_dict = { 'name': 'Fahad', 'age' : 11}

print(my_dict)
print(my_dict['name'])
print(my_dict.get('age'))

my_dict['address'] = 'London'
print(my_dict)
print(my_dict.pop('address'))
print(my_dict)

my_tuple = ('p', 'e', 'r', 'm','i', 't')
print(my_tuple[0])
print(my_tuple[1])
print(my_tuple[2])
print(my_tuple[3])
print(my_tuple[4])
print(my_tuple[5])

print(my_tuple[1:4])
for i in my_tuple:
    print(i)