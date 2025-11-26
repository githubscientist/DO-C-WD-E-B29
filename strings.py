# fruit = 'apple'

# Methods
# print(fruit.find('z'))

# print(fruit.swapcase())

# Slicing
# print(fruit[0:5:2])

# sentence = 'apple is a fruit'
# print(sentence)  # "apple is a fruit"
# print(sentence[3])  # "l"
# print(sentence[3:10])  # "le is a"
# print(sentence[3:10:2])  # "l sa"

'''
Given a string, count the number of vowels in it and print the count.

Note: vowels are 'a', 'e', 'i', 'o', 'u'

Example: 

s = 'apple'

vowels = 2

s = 'orange'

vowels = 3
'''

# get the string from the user
s = input('enter a string to count the vowels: ')

# intialize a counter to keep track of the number of vowels in the string
vowels = 0

index = 0
while index < len(s):
    # check if that character is a vowel
    if s[index] == 'a' or s[index] == 'e' or s[index] == 'i' or s[index] == 'o' or s[index] == 'u':
        vowels = vowels + 1
    index = index + 1

print(vowels)
