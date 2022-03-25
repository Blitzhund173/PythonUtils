from keyboard import wait,is_pressed
from pyautogui import click
import threading


def autoclick():
    while True:
        click()
        if is_pressed("f")==True:
                break


thread0=threading.Thread(target=autoclick, args=())
thread1=threading.Thread(target=autoclick, args=())
thread2=threading.Thread(target=autoclick, args=())
thread3=threading.Thread(target=autoclick, args=())
thread4=threading.Thread(target=autoclick, args=())
thread5=threading.Thread(target=autoclick, args=())

while True:
    wait("q")
    thread0.start()
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()
    thread0.join()
    break

quit