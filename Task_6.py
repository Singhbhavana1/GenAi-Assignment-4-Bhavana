
import os

filename = input("Enter file name: ")

if os.path.exists(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
            print(content)

    except PermissionError:
        print("Permission denied")

else:
    print("File not found. Please check the filename.")
