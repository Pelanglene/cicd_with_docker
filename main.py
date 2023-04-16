import time 
import logging 

if __name__ == '__main__':
    times = 0
    while True:
        with open("test.txt", "a") as file:
            file.write(str(int(time.time())))
        
        time.sleep(3)
        times += 1
        if times == 3:
            break

