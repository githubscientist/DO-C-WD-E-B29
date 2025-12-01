# with open('/Users/sathish/Desktop/records.txt', 'r') as f:
#     fileContents = f.read()
#     print(len(fileContents.split('\n')))


with open('/Users/sathish/Desktop/records.txt', 'r') as f:
    # get the contents of the file
    data = f.read().split('\n')

with open('/Users/sathish/Desktop/records.txt', 'w') as f:
    data.insert(0, 'User 1030 accessed the system at 2024-06-15 14:22:19')
    f.write('\n'.join(data))
