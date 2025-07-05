from tkinter.filedialog import * 
from tkinter import ttk
import tkinter as tk

canvas = tk.Tk() 

def saveFile():
    file_path = asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if not file_path:
        return
    with open(file_path, "w") as file:
        text = entry.get(1.0, tk.END)
        file.write(text)

def openFile():
    file_path = askopenfilename(filetypes=[("Text files", "*.txt")])
    if not file_path:
        return
    with open(file_path, "r") as file:
        content = file.read()
        entry.delete(1.0, tk.END)  
        entry.insert(tk.INSERT, content)

def clearFile():
    entry.delete(1.0, tk.END)


canvas.geometry("800x600")
canvas.config(bg="white")
canvas.title("Notepad")
top = tk.Frame(canvas, bg="white")
top.pack(padx = 10, pady = 10, anchor="nw")

b1 = tk.Button(canvas, text="Open", bg="white", command = openFile)
b1.pack(in_= top, side = tk.LEFT)
b2 = tk.Button(canvas, text="Save", bg="white", command = saveFile)
b2.pack(in_= top, side = tk.LEFT)
b3 = tk.Button(canvas, text="Clear", bg = "white", command = clearFile)
b3.pack(in_= top, side = tk.LEFT)

entry = tk.Text(canvas, bg="white", font=("Arial", 12), wrap=tk.WORD)
entry.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)
canvas.mainloop()
