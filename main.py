import tkinter as tk
#messagebox
from tkinter import messagebox

class MyGUI:
  def __init__(self):
    self.root = tk.Tk() #windom
    self.root.geometry("400x400") #sides of windom
    self.root.title("My First GUI")
    
    self.label = tk.Label(self.root, text="Your Message", font=('Arial', 18))
    self.label.pack(padx=10, pady=10)
    
    self.textbox = tk.Text(self.root, height=5, font=('Arial', 16))
    self.textbox.pack(padx=10, pady=10)
    #show messagebox
    self.check_state = tk.IntVar()
    self.check = tk.Checkbutton(self.root, text="Show Messagebox", font=('Arial', 16), variable=self.check_state)
    self.check.pack(padx=10, pady=10)
    
    self.button = tk.Button(self.root, text="Click Me!", font=('Arial', 18), command=self.on_click)
    self.button.pack(padx=10, pady=10)
    
    self.root.mainloop()
  def on_click(self):
    #
    print(self.check_state.get())
    #show messagebox
    if self.check_state.get() == 0:
      print(self.textbox.get('1.0', tk.END))
    else:
      messagebox.showinfo(title="Message", message=self.textbox.get('1.0', tk.END))

MyGUI()