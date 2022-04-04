from keyboard import wait,is_pressed
from pyautogui import click
import threading

#Defines the main clicking function
def autoclick(threadnum):
    #Murders the cpu
    while True:
        click()
        #If the user presses the "f" key, the program will end
        if is_pressed("f"):
            print(f"Thread {threadnum} has ended")
            break

#Defines threads in a list
threads = []
for i in range(10):
    threads.append(threading.Thread(target=autoclick,args=(i,)))


#Waits for "q" then starts all the threads
wait("q")
for i in range(10):
    threads[i].start()