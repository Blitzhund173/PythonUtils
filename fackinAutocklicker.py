from keyboard import wait,is_pressed
from pyautogui import click
import threading

#Defines the main clicking function
def autoclick():
    #Murders the cpu
    while True:
        click()
        #Checks if the f key is pressed and if so it exits
        if is_pressed("f")==True:
                break

#Defines all threads
thread0=threading.Thread(target=autoclick, args=())
thread1=threading.Thread(target=autoclick, args=())
thread2=threading.Thread(target=autoclick, args=())
thread3=threading.Thread(target=autoclick, args=())
thread4=threading.Thread(target=autoclick, args=())
thread5=threading.Thread(target=autoclick, args=())

#Waits for "q" then starts all the threads
wait("q")
thread0.start()
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()
#Waits until the thread exits
thread0.join()

#Just quits because you cant start a dead thread
quit()