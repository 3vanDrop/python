from tkinter import *
 
window = Tk()
 
window.title("Welcome to LikeGeeks app")
 
window.geometry('350x200')
 
spin = Spinbox(window, from_=0, to=100, width=5)
 
spin.grid(column=0,row=0)
 
window.mainloop()
