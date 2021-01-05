ex = [1,2,3,4,5]

print(list(map(lambda x: x+x, ex)))
print((map(lambda x: x+x, ex)))

f = lambda x: x**2
print(map(f, ex))
for i in map(f, ex):
    print(i)

result = (map(f, ex))
print(next(result))