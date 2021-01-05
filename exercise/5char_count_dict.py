from collections import Counter

message = \
    "It was a bright cold day in April, " \
    "and the clocks were striking thirteen."
print(dict(Counter(message)))
