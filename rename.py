import os

xtn = input("What extension?:\n")

dir_name = '.'

list_of_files = sorted( filter( lambda x: os.path.isfile(os.path.join(dir_name, x)),os.listdir(dir_name) ) )

nums = []
for i in range(len(str(len(list_of_files)))):
    nums += [0]

for file in list_of_files:
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

    print(file + f" --> {str(num)}.{xtn}") 
    os.system(f"mv '{file}' '{str(num)}.{xtn}'")
