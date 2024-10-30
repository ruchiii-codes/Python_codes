# write a python program to prints the contents of a directory using the os modules. search online for the function which does that. 

import os

# Function to print the contents of a directory
def print_directory_contents(path='/'):
    try:
        # List all files and directories in the given path
        contents = os.listdir(path)
        print(f"Contents of the directory '{path}':")
        for item in contents:
            print(item)
    except FileNotFoundError:
        print(f"The directory '{path}' does not exist.")
    except PermissionError:
        print(f"Permission denied for accessing the directory '{path}'.")

# Test the function with the current directory
print_directory_contents()
