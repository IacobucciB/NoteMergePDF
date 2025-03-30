import tkinter as tk
from tkinter import ttk

class App:
    def __init__(self):
        self.root = self.__create_root()
    
    def __create_root(self):
        root = tk.Tk()
        root.tk.call('tk', 'scaling', 2.0)
        root.title("Note Merge PDF")
        root.option_add("*tearOff", False)
        root.geometry("800x600")
        root.tk.call("source", "Forest-ttk-theme/forest-dark.tcl")
        ttk.Style().theme_use("forest-dark")
        return root
    
    def start_mainloop(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = App()
    app.start_mainloop()