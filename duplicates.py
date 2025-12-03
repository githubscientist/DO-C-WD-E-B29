'''
    count the frequencies
    removing the duplicates or having only the unique elements

    hashing technique
'''

# aabdbacdefeflkjsdfckskfkwebrwenb
# s = 'apple is a fruit'

# d = {}

# for char in s:
#     d[char] = 0

# for char in s:
#     d[char] = d[char] + 1

# print(d)


# s = [1, 2, 3, 4, 5, 6, 4, 3, 4, 5, 3, 2]

# d = {}

# for char in s:
#     d[char] = 0

# for char in s:
#     d[char] = d[char] + 1

# print(d)

s = ['apple', 'banana', 'apple', 'orange', 'apple']

d = {}

for char in s:
    d[char] = 0

for char in s:
    d[char] = d[char] + 1

print(d)
