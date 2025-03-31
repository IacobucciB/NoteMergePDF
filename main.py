import tkinter as tk
from tkinter import ttk
import logging
import os
import sys
from merge_lib import merge_pdfs, get_pdf_page_counts, merge_selected_pages

class App:
    def __init__(self):
        self.root = self.__create_root()
        self.pdf_files = []
    
    def __create_root(self):
        root = tk.Tk()
        root.tk.call('tk', 'scaling', 1.5)
        root.title("Note Merge PDF")
        root.option_add("*tearOff", False)
        root.geometry("900x600")
    
        if hasattr(sys, '_MEIPASS'):
            theme_path = os.path.join(sys._MEIPASS, "Forest-ttk-theme", "forest-dark.tcl")
        else:
            theme_path = os.path.join(os.getcwd(), "Forest-ttk-theme", "forest-dark.tcl")
    
        if os.path.exists(theme_path):
            root.tk.call("source", theme_path)
            ttk.Style().theme_use("forest-dark")
        else:
            print(f"Error: No se encontró el archivo {theme_path}")
        return root

    def create_layout(self):
        self.root.columnconfigure(0, weight=3)
        self.root.columnconfigure(1, weight=7)
        self.root.rowconfigure(0, weight=1)

        left_frame = tk.Frame(self.root, bg="#2b2b2b", padx=10, pady=10)
        left_frame.grid(row=0, column=0, sticky="nsew")
        left_frame.rowconfigure(0, weight=1)
        left_frame.rowconfigure(1, weight=0)
        left_frame.columnconfigure(0, weight=1)
        left_frame.columnconfigure(1, weight=0)

        right_frame = tk.Frame(self.root, bg="#2b2b2b", padx=10, pady=10)
        right_frame.grid(row=0, column=1, sticky="nsew")
        right_frame.rowconfigure(0, weight=1)
        right_frame.rowconfigure(1, weight=0)
        right_frame.columnconfigure(0, weight=1)
        right_frame.columnconfigure(1, weight=0)

        self.create_buttons(left_frame)
        self.create_right_panel(right_frame)

    def create_buttons(self, parent):
        self.file_listbox = tk.Listbox(parent, bg="#1e1e1e", fg="white", selectbackground="#3a3a3a", relief="flat")
        self.file_listbox.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

        file_scrollbar = ttk.Scrollbar(parent, orient="vertical", command=self.file_listbox.yview)
        file_scrollbar.grid(row=0, column=1, sticky="ns", padx=5)
        self.file_listbox.config(yscrollcommand=file_scrollbar.set)

        button_frame = tk.Frame(parent, bg="#2b2b2b")
        button_frame.grid(row=1, column=0, columnspan=2, sticky="ew", padx=5, pady=5)

        self.up_button = ttk.Button(button_frame, text="Up", command=self.__move_up)
        self.up_button.grid(row=0, column=0, padx=5)

        self.down_button = ttk.Button(button_frame, text="Down", command=self.__move_down)
        self.down_button.grid(row=0, column=1, padx=5)

        self.select_files_button = ttk.Button(parent, text="Select Files", command=self.__getfiles)
        self.select_files_button.grid(row=2, column=0, columnspan=2, sticky="ew", padx=5, pady=5)

        self.split_button = ttk.Button(parent, text="Split", command=self.__split_files)
        self.split_button.grid(row=3, column=0, columnspan=2, sticky="ew", padx=5, pady=5)

        self.merge_button = ttk.Button(parent, text="Merge", command=self.__merge_files)
        self.merge_button.grid(row=4, column=0, columnspan=2, sticky="ew", padx=5, pady=5)

    def create_right_panel(self, parent):
        self.page_listbox = tk.Listbox(parent, bg="#1e1e1e", fg="white", selectbackground="#3a3a3a", relief="flat")
        self.page_listbox.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

        page_scrollbar = ttk.Scrollbar(parent, orient="vertical", command=self.page_listbox.yview)
        page_scrollbar.grid(row=0, column=1, sticky="ns", padx=5)
        self.page_listbox.config(yscrollcommand=page_scrollbar.set)

        button_frame = tk.Frame(parent, bg="#2b2b2b")
        button_frame.grid(row=1, column=0, columnspan=2, sticky="ew", padx=5, pady=5)

        self.page_up_button = ttk.Button(button_frame, text="Up", command=self.__move_page_up)
        self.page_up_button.grid(row=0, column=0, padx=5)

        self.page_down_button = ttk.Button(button_frame, text="Down", command=self.__move_page_down)
        self.page_down_button.grid(row=0, column=1, padx=5)

        self.page_merge_button = ttk.Button(button_frame, text="Merge", command=self.__merge_pages)
        self.page_merge_button.grid(row=0, column=2, padx=5)

    def __getfiles(self):
        current_folder = os.getcwd()
        pdf_files = [f for f in os.listdir(current_folder) if f.endswith('.pdf')]
        self.pdf_files.extend(pdf_files)
        self.file_listbox.delete(0, tk.END)
        for file in pdf_files:
            self.file_listbox.insert(tk.END, file)
        logging.basicConfig(level=logging.INFO)
        logging.info(f"Automatically selected files: {pdf_files}")
        logging.info(f"Files in App: {self.pdf_files}")
        
    def __merge_files(self):
        if not self.pdf_files:
            logging.warning("No files selected for merging.")
            return
        logging.info(f"Merging files: {self.pdf_files}")
        merge_pdfs(self.pdf_files)
        logging.info("Merge operation completed.")

    def __split_files(self):
        if not self.pdf_files:
            logging.warning("No files selected for splitting.")
            return
        self.page_listbox.delete(0, tk.END)
        for pdf in self.pdf_files:
            page_counts = get_pdf_page_counts([pdf])
            for file, pages in page_counts:
                for page in range(1, pages + 1):
                    self.page_listbox.insert(tk.END, f"{file} - Page {page}")
        logging.info("Files split by pages and displayed in the right panel.")

    def __move_up(self):
        selected_index = self.file_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            if index > 0:
                self.file_listbox.delete(index)
                self.file_listbox.insert(index - 1, self.pdf_files[index])
                self.file_listbox.selection_set(index - 1)
                self.pdf_files[index], self.pdf_files[index - 1] = self.pdf_files[index - 1], self.pdf_files[index]

    def __move_down(self):
        selected_index = self.file_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            if index < len(self.pdf_files) - 1:
                self.file_listbox.delete(index)
                self.file_listbox.insert(index + 1, self.pdf_files[index])
                self.file_listbox.selection_set(index + 1)
                self.pdf_files[index], self.pdf_files[index + 1] = self.pdf_files[index + 1], self.pdf_files[index]

    def __move_page_up(self):
        selected_index = self.page_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            if index > 0:
                item = self.page_listbox.get(index)
                self.page_listbox.delete(index)
                self.page_listbox.insert(index - 1, item)
                self.page_listbox.selection_set(index - 1)

    def __move_page_down(self):
        selected_index = self.page_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            if index < self.page_listbox.size() - 1:
                item = self.page_listbox.get(index)
                self.page_listbox.delete(index)
                self.page_listbox.insert(index + 1, item)
                self.page_listbox.selection_set(index + 1)

    def __merge_pages(self):
        selected_pages = self.page_listbox.get(0, tk.END)
        if not selected_pages:
            logging.warning("No pages selected for merging.")
            return
        logging.info(f"Merging pages: {selected_pages}")
        try:
            merge_selected_pages(selected_pages)
            logging.info("Page merge operation completed.")
        except Exception as e:
            logging.error(f"Error during page merge operation: {e}")

    def start_mainloop(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = App()
    app.create_layout()
    app.start_mainloop()