my_str = 'java python kotlin'
my_list = my_str.split()
print(type(my_list), my_list)

my_str2 = ''.join(my_list)
print(my_str2)

my_str = 'java,python,kotlin'
my_list2 = my_str.split(',')
print(my_list2)
my_str2 = ','.join(my_list2)
print(my_str2)
