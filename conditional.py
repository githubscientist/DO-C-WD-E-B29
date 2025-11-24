'''
Types of Conditional Statements
    1. if condition
    2. if...else condition
    3. Multiple if...else condition (if...elif...else)
    4. Nested if...else statement
'''

# if statement
# # Given a number, print the absolute value of the number
# number = -5

# # check if the number is a negative number
# if number < 0:
#     # if the number is negative, convert it to a positive number
#     number = number * -1

# # print the number
# print(number)

# if...else statement
# '''
#     Given a number, check and print if the number is a positive number or a negative number
# '''
# number = 0

# # check if the number is a positive number
# if number > 0:
#     # print its a positive number
#     print(number, 'is a Positive Number')
# else:
#     # the number is negative
#     print(number, 'is a Negative Number')

# Nested if...else statement

'''
    Given a number, check and print if the number is a positive number or a negative number or a zero
'''

# number = 0

# if number > 0:
#     # the number is a positive number
#     print(number, 'is a positive number')
# else:
#     # definitely the number is a not a positive number
#     # either the number can be a negative number or a zero
#     # have to decide whether the number is a negative or a zero
#     if number < 0:
#         # the number is a negative number
#         print(number, 'is a negative number')
#     else:
#         # the number definitely has to be a zero
#         print(number, 'is a zero')

'''
    Given a number, check and print if the number is a positive number or a negative number or a zero
'''

number = 0

if number > 0:
    # the number is a positive number
    print(number, 'is a positive number')
elif number < 0:
    # the number is a negative number
    print(number, 'is a negative number')
else:
    # definitely the number has to be a zero
    print(number, 'is a zero')
