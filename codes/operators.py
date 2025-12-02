'''
    Voting Eligibility

    Given:
        age
        hasAadhar
        hasVoterID

    Eligibility Criteria:
        - Age of the person should be greater than or equal to 18.
        - The person should have one of the following IDs:
            - Aadhar Card
            - Voter ID
'''

# age = 25
# hasAadhar = True
# hasVoterID = True

# # age is greater than or equal to 18 and has an aadhar card or has a voter id
# if (age >= 18) and (hasAadhar or hasVoterID):
#     print('You are Eligible to Vote!')
# else:
#     print('You are Not Eligible to Vote!')


'''
    Given a number, print the absolute value of the number.
'''

number = -5

# check if the number is a negative number
if number < 0:
    number = number * -1

# we have to print only the positive form of the number
print(number)

'''
    Variables -> used to store values in the memory
    Data Types -> tells which type of value we can store in a variable
    Operators -> tells which type of operation we can perform in that variable or with additional variables
    -----
    Conditional Statements -> to do a decision making
    Looping Statements -> to execute a block of code repetitively
    Functions -> to execute a block of code whenever or only when we need it
'''
