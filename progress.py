#!/usr/bin/python3
import os

while True:
    try:
        os.system('sudo progress -w || break')
    except:
        print("progress is not installed, installing...")
        os.system("sudo apt install progress --install-recommends -y")