from time import sleep
import keyboard
import tkinter as tk
from tkinter import ttk

#Sets up tkinter
root=tk.Tk()
root.title("Send message")
root.geometry("300x200")
root.resizable(False, False)

#Makes a label saying "Send message" and centres it
tk.Label(root, text="Send message").grid(row=1,column=5)

text=""

#Repeats the text times times
def send(times):
    print("Sending message")
    for i in range(times):
        keyboard.write(text)
        keyboard.press_and_release("enter")
        sleep(1)

textInput=tk.Entry(root,textvariable=text)

#Gets reps from a tkinter entry
repsNum=0
reps=tk.Entry(root,textvariable=repsNum)
reps.grid(row=1,column=5)


#Get number of times to type the text
try:
    times = int(reps.get())
except:
    ttk.Label(root, text="Please enter a number").grid(row=2,column=5)

#Sets up the sendButton
sendButton=ttk.Button(
    root,
    text="Send",
    command=lambda:send(times)
)
sendButton.grid(row=5,column=5)

try:
    from ctypes import windll

    windll.shcore.SetProcessDpiAwareness(1)
finally:
    root.mainloop()