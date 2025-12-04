import os

# print the current location
# print(os.getcwd())

# print all the files and directories in the current path
listdirs = os.listdir()

# print all the files and folders in a new line
for item in listdirs:
    # check if it is a folder or a file
    # folders
    if os.path.isdir(item):
        # these items are folders
        # if it is a directory, let's print all the files in that directory
        print(item)

        # print all the files and directories in that folder
        subdirs = os.listdir(os.path.join(os.getcwd(), item))

        print('   --', '\n   -- '.join(subdirs))
    else:
        print(item)
