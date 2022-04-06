from time import sleep
import keyboard
import tkinter as tk
from tkinter import ttk

#Sets up tkinter
root=tk.Tk()
root.title("Send message")
root.geometry("300x200")
root.resizable(False, False)

#Preloads the text
kounterText=ttk.Label(root, text=f"5 Seconds and counting...")
kounterText.grid(row=9,column=5)


#Sets up some variables for later
times=0
text=""

#Repeats the text times times
def send(times):
    sleep(5)
    for i in range(times):
        keyboard.write(text)
        keyboard.press_and_release("enter")
        sleep(1)

#Gets the text from the entry box and sets it to text
ttk.Entry(root,textvariable=text).grid(row=1,column=5)
ttk.Label(root, text="Text").grid(row=3,column=5)


#Gets reps from a tkinter entry
ttk.Entry(root,textvariable=times).grid(row=5,column=5)
#Labels the entry
ttk.Label(root, text="Times").grid(row=7,column=5)


#Sets up the sendButton
sendButton=ttk.Button(
    root,
    text="Send",
    command=lambda:send(times)
)
sendButton.grid(row=5,column=7)

try:
    from ctypes import windll

    windll.shcore.SetProcessDpiAwareness(1)
finally:
    root.mainloop()