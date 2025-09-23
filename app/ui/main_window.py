import tkinter as tk
from tkinter import ttk

class MainWindow(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master, bg="#f6f6f6")
        self.controller = controller
        self.pack(fill="both", expand=True)
        self._build()

    def _build(self):
        # Task dropdown (empty for now)
        top = tk.Frame(self, bg="#f6f6f6")
        top.pack(fill="x", padx=10, pady=10)

        tk.Label(top, text="Select Task:", font=("Segoe UI", 10)).pack(side="left")
        self.task_var = tk.StringVar()
        self.task_combo = ttk.Combobox(top, textvariable=self.task_var, state="readonly", values=[])
        self.task_combo.pack(side="left", padx=5)

        # Input panel
        tk.Label(self, text="Input:", font=("Segoe UI", 10, "bold")).pack(anchor="w", padx=10, pady=(10, 0))
        self.input_txt = tk.Text(self, height=6, wrap="word")
        self.input_txt.pack(fill="x", padx=10, pady=(0, 10))

        # Output panel
        tk.Label(self, text="Output:", font=("Segoe UI", 10, "bold")).pack(anchor="w", padx=10, pady=(10, 0))
        self.output_txt = tk.Text(self, height=6, wrap="word", state="disabled")
        self.output_txt.pack(fill="x", padx=10, pady=(0, 10))

        # Info panel placeholder
        tk.Label(self, text="Model Info (to be added later)", fg="grey").pack(pady=20)
