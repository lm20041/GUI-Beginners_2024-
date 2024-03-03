# Create a window
import tkinter as tk 
root = tk.Tk() 
#sides of the window
root.geometry("2500,2500")
#title of the window
root.title("My First GUI")
#create a label
label = tk.Label(root, text="Hello World!", fron=('Arial', 18))
#place the label in the window
label.pack(padx=20, pady=20)
#place the textbox in the window
textbox = tk.Text(root, height=3, font=('Arial', 16))
textbox.pack()
#place the Entry in the window
myentry = tk.Entry(root)
myentry.pack()

root.mainloop()