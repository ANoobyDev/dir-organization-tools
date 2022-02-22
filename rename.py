import os

list_of_files = sorted( filter( lambda x: os.path.isfile(os.path.join(".", x)),os.listdir(".") ) )

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
    os.system(f"mv '{file[0]}' '{str(num)}{xtn}' 2>/dev/null")
