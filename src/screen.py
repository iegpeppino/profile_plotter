import tkinter as tk
from tkinter import ttk, filedialog
import os

class MainMenu(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # screen_width = self.winfo_screenwidth()
        # screen_height = self.winfo_screenheight()
        # self.geometry(f"{screen_width}x{screen_height}")
        self.geometry("800x600")
        self.title("Perfiles de Carga")
        self.folder_path = "data"
        self.files = os.listdir(self.folder_path)    

        self.file_dropdown = ttk.Combobox(self, values=self.files, state="readyonly")
        self.file_dropdown.pack(pady=10)
        self.file_dropdown.bind("<<ComboboxSelected>>", lambda event: set_file(self.file_dropdown.get()))

        self.selected_file_label = tk.Label(self, text="Selected file: None")        
        self.selected_file_label.pack()
        
        def set_file(filename):
            self.selected_file_label.config(text=f"Selected File: {filename}")



