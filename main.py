import requests
import tkinter as tk
import json

wind=tk.Tk()
wind.title("Phonebomb")
wind.geometry("500x200")

tk.Label(wind, text="Phone number").grid(row=0)
tk.Label(wind, text="Message").grid(row=1)

ent1=tk.Entry(wind)
ent2=tk.Entry(wind)

ent1.grid(row=0, column=1) 
ent2.grid(row=1, column=1)

def getStatus(textId):
    MoreInfo=requests.get("https://textbelt.com/status/"+textId)
    MoreInfo=str(MoreInfo.text)

    mLoaded=json.loads(MoreInfo)
    return(mLoaded["status"])


def func():#function of the button
    resp = requests.post('https://textbelt.com/text', {
    'phone': ent1.get(),
    'message': ent2.get(),
    'key': 'textbelt',
    })
    response=resp.json()
    response=str(response)

    response=response.replace("'","\"")
    response=response.replace("True","true")
    response=response.replace("False","false")

    jLoaded=json.loads(response)

    if str(jLoaded["success"])=="True":
        print("Partial succsess")
        print(getStatus(jLoaded["textId"]))
        
    else: 
        print("Error:",jLoaded["error"])
        
    
    
btn=tk.Button(wind,text="Bomb", width=10,height=5,command=func)
btn.place(x=200,y=70)

wind.mainloop()