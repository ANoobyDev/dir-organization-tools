import os

files=os.listdir()
print(files)

for filz in files:
    os.system(f'unzip "{filz}" && rm "{filz}"')
