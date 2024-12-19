# Write a python program to print the contents of a directory using the os module.
# Search online for the function which does that.

import os

# Specify the directory path (use '.' for the current directory)
directory_path = '/Old folder'

# List the contents of the directory
contents = os.listdir(directory_path)

# Print the contents
for item in contents:
    print(item)
    