path = 'yesterday.txt'
file = open(path, 'r')

upper_count = 0
capital_count = 0
lower_count = 0

lines = file.readlines()
for line in lines:
    upper_count += line.upper().count("YESTERDAY")
    capital_count += line.count("Yesterday")
    lower_count += line.count("yesterday")

print("YESTERDAY 개수: {0}".format(upper_count))
print("Yesterday 개수: {0}".format(capital_count))
print("yesterday 개수: {0}".format(lower_count))