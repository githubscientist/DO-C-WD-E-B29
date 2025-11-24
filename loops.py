# while loop
# noOfTimes = int(input("How many hello do you want?"))
# count = 0
# while count < noOfTimes:
#     print("hello")
#     count = count + 1


# 1, 2, 3, 4, 5
# noOfTimes = int(input("How many hello do you want?"))
# for count in range(0, noOfTimes, 1):
#     print("hello")

# while...else loop
# count = 0
# while count < 3:
#     print("hello")
#     count = count + 1
# else:
#     print("printed after a uninterrupted while execution")

number = int(input('which multiplication table ?'))
count = 1
# stopping condition: count <= 10
while count <= 10:
    print(number, 'x', count, '=', number * count)
    count = count + 1
