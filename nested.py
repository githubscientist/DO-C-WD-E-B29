range = int(input('enter the range to print factorials from 1 to range: '))

iterations = 1
while iterations <= range:
    # initialize result variable with the value 1
    result = 1

    num = iterations

    # run a loop iteratively until num > 1
    while num > 1:
        # find the product of result * num and store the result back to result
        result = result * num

        # reduce the num by 1 and store it back to num
        num = num - 1

    # print the result value
    print(iterations, '!', ' = ', result, sep='')

    iterations = iterations + 1
