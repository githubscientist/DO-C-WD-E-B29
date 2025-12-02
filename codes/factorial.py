# # get the input number from the user
# num = int(input('enter a number to find its factorial: '))

# # initialize result variable with the value 1
# result = 1

# # run a loop iteratively until num > 1
# while num > 1:
#     # find the product of result * num and store the result back to result
#     result = result * num

#     # reduce the num by 1 and store it back to num
#     num = num - 1

# # print the result value
# print(result)


# -------------------

# get the input number from the user
num = int(input('enter a number to find its factorial: '))

# initialize result variable with the value 1
result = 1

# run a loop iteratively until num > 1
for i in range(1, num+1, 1):
    # find the product of result * num and store the result back to result
    result = result * i

# print the result value
print(result)
