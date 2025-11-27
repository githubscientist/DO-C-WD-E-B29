fruits = ['apple', 'orange', 'apple', 'banana', 'orange', 'orange']

# create a dictionary to store the frequencies of the numbers
frequencies = {}

for fruit in fruits:
    # create an entry in the frequencies dictionary
    frequencies[fruit] = 0

for fruit in fruits:
    # create an entry in the frequencies dictionary
    frequencies[fruit] = frequencies[fruit] + 1

print(frequencies)

'''
    fruit = 'banana'

    frequencies = {
        "orange" : 3,
        "banana" : 1,
        "cherries" : 2
    }

    frequencies["cherries"] = frequencies["apple"]
    del frequenices["apple"]

    frequencies[fruit] = frequencies[fruit] + 1
    frequencies[fruit] = frequencies['apple'] + 1
    frequencies[fruit] = 0 + 1
    frequencies['apple'] = 1



    "apple": 2
    "orange": 3
    "banana" 1
'''
