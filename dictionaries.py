# gets the fruit name from the user and returns its price per kg

# fruits = [['apple', 240], ['orange', 100],
#           ['pomegranate', 300], ['grapes', 50]]

# fruitInput = input('Enter a fruit to get its price: ')

# # Iterate the fruits list from the first fruit till the last fruit in the list
# for fruit in fruits:
#     if fruit[0] == fruitInput:
#         print(fruit[0], 'costs', fruit[1], 'rupees per kg')

# fruits = {
#     "apple": 240,
#     "orange": 100,
#     "pomegranate": 300,
#     "grapes": 50
# }

# fruitInput = input('Enter a fruit to get its price: ')

# print(fruitInput, 'costs', fruits[fruitInput], 'rupees per kg')

# fruits = {
#     "apple": 240,
#     "orange": 100,
#     "pomegranate": 300,
#     "grapes": 50
# }

# fruits['banana'] = 75

# del fruits['orange']

# fruits['apple'] = fruits['apple'] + 20

# print(fruits)

# fruits = {
#     "apple": 240,
#     "orange": 100,
#     "pomegranate": 300,
#     "grapes": 50
# }

# for key in fruits:
#     print(fruit, fruits[key])

# Create a dictionary with all your details you provide in your resume.
# name, profession, hobbies, cgpa, location
resume = {
    "name": "krish",
    "profession": "developer",
    "hobbies": ["cooking", 'driving', 'fishing'],
    "cgpa": 8.78,
    "location": "India"
}


# Add a new entry to the dictionary -- company
resume['company'] = 'Toptal'

# Print the total number of items in the dictionary
# print(len(resume))

# Print the name and hobbies using for loop
for key in resume:
    if key == 'name' or key == 'hobbies':
        print(key, ':', resume[key])

# delete the cgpa key
del resume['cgpa']

print(resume)
