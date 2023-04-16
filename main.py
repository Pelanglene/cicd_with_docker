import time 
import logging 
import os
import subprocess

if __name__ == '__main__':
    times = 0
    os.system("pwd")
    while True:
        with open("data/test" + str(time.time()) + ".txt", "a") as file:
            file.write(str(int(time.time())))
        print(time.time())
        time.sleep(3)
        times += 1
        if times == 3:
            break
