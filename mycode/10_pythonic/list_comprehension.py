result = [x for x in range(10) if x%2 == 0]
print(result)

my_str1 = "Hello"
my_str2 = "World"

result = [i+j for i in my_str1 for j in my_str2 if not (i==j)]
print(result)
