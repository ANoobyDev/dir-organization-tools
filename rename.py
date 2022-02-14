import os

xtn=input("What extension?")

dir_name = '.'

list_of_files = sorted( filter( lambda x: os.path.isfile(os.path.join(dir_name, x)),os.listdir(dir_name) ) )

num1 = num2 = 0

for file in list_of_files:
    num1=num1+1
    if num1==10:
        num1=0
        num2=num2 + 1
    num = str(num2)+str(num1)
    print(file)
    os.system(f"mv '{file}' '{str(num)}'.{xtn}")
