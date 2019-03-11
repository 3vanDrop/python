from tkinter import *
 
window = Tk()
 
window.title("Welcome to LikeGeeks app")
 
lbl = Label(window, text="Hello")
 
lbl.grid(column=0, row=0)

lbl = Label(window, text="Hello Big font", font=("Arial Bold", 50))
 
window.mainloop()
