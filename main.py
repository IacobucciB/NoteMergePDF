import tkinter as tk
from tkinter import ttk

def create_window():
    window = tk.Tk()
    window.tk.call('tk', 'scaling', 2.0)
    window.title("Note Merge PDF")
    window.option_add("*tearOff", False)
    window.geometry("800x600")

    window.tk.call("source", "Forest-ttk-theme/forest-dark.tcl")
    ttk.Style().theme_use("forest-dark")
    
    
    label = ttk.Label(window, text="Hello, Tkinter with Theme!", font=("Roboto", 12))
    label.pack(pady=20)
    
    button = ttk.Button(window, text="Close", command=window.destroy)
    button.pack(pady=10)
    
    window.mainloop()

if __name__ == "__main__":
    create_window()