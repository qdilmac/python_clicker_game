# Another basic GUI program beacuse why not
# Simple Clicker Game
# Author: Mustafa Osman Dilmaç

import tkinter as tk
from tkinter import ttk
import random as rnd

clicked = 0
def click():
    global clicked
    clicked = int(counter_label.cget("text")) #gets the value if luck button pressed first
    clicked += 1
    counter_label.config(text=str(clicked))

rand_click = 0
is_used = False
def luck():
    global is_used
    if is_used == False:
        rand_click = rnd.randint(-100,100)
        counter_label.config(text=str(rand_click))
        is_used = True
    else:
        print("One time use only.")

def refresh():
    global is_used
    counter_label.config(text=str(0))
    if is_used == True:
        is_used = False

def main():
    root = tk.Tk()
    root.title("Simple Clicker GUI")
    root.geometry("320x160")
    global counter_label
    counter_label = tk.Label(root,text=0,fg="red",pady=20)
    counter_label.pack()

    add_button = tk.Button(root,text="Click Me",command=click)
    add_button.pack()

    luck_button = tk.Button(root,text="Feeling Lucky?",command=luck)
    luck_button.pack()

    refresh_button = tk.Button(root, text="Refresh!",command=refresh)
    refresh_button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()