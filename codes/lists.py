# values = [192, 'apple', True, 8.78]

# print(values)  # [192, 'apple', True, 8.78]

# print(values[0])  # 192

# reverse indexing
# print(values[-1]) # 8.78

# assign or update values at a index because lists are mutables (changeables)
# values[0] = 200

# print(values) # [200, 'apple', True, 8.78]

# word = 'apple'

# print(word)  # 'apple'
# print(word[0])  # 'a'

# the following throws error as strings are immutables (or unchangeables)
# word[1] = 'm'
# print(word)

# result: 'ample'
# word = 'apple'
# index = 1
# char = 'm'
# word = word[0:index] + char + word[index+1:]

# print(word)

# l = ['apple']

# # l[0] = 'orange'
# l[0] = l[0][0:1] + 'm' + l[0][2:]

# print(l[0][1])
# print(l)

# slicing in lists
# values = [192, 'apple', True, 8.78]

# # print(values)  # [192, 'apple', True, 8.78]
# # print(values[0])  # 192
# print(values[0:4:3])

# values = [192, 'apple', True, 8.78, 'apple']
# values.append('python')
# values.insert(2, 'python')
# values.clear()

# values.pop(0)

# values.remove('apple')
# values.remove('apple')

# print(values)

# iterating a list
# values = [3, 6, 1, 5, 4, 2]

# index = 0
# while index < len(values):
#     if values[index] >= 5:
#         print(values[index])
#     index = index + 1
