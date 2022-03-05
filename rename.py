#!/usr/bin/python3
import os
from sys import argv

# Get where the dir will act
if len(argv) == 2:
    dirc = argv[1]
else:
    dirc = "."

# Check if last char of the directory is '/', and if it is, remove it
if dirc[-1] == '/':
    dirc[-1] == ''

# Get sorted list of the dir
list_of_files = sorted(os.listdir(dirc))

nums = []
for i in range(len(str(len(list_of_files)))):
    nums += [0]

for file in list_of_files:
    # Gets the extension
    preFile = file
    file = file.split(".")
    
    try:
        xtn = "." + file[1]
    except:
        xtn = "." + input(f"Extension for {file[0]}?: ")

    nums[-1] += 1
    if nums[-1] == 10:
        nums[-1] = 0
        nums[-2] += 1
        if nums[-2] == 10:
            nums[-2] = 0
            nums[-3] += 1
            if nums[-3] == 10:
                nums[-3] = 0
                nums[-4] += 1

    num = ""
    for i in nums:
        num = num + str(i)

    print(preFile + f" --> {str(num)}{xtn}") 
    os.system(f"mv '{dirc}/{preFile}' '{dirc}/{str(num)}{xtn}'")
