#!/usr/bin/python3
import os

extension=input("Extension of images: ")
for i in range(100):
    raw_num=f"00000{i}"
    num=raw_num[len(raw_num)-3]+raw_num[len(raw_num)-2]+raw_num[len(raw_num)-1]
    os.system(f"mv {i}.{extension} {num}.{extension}")

