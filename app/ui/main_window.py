import tkinter as tk
from tkinter import ttk, messagebox
from typing import Dict, Any

OOP_EXPLANATION = (
    "OOP Concepts in this App:\n"
    "• Encapsulation: model internals stored in private attributes (e.g., _model).\n"
    "• Polymorphism: all models expose the same run(input) interface via BaseModel.\n"
    "• Method Overriding: concrete models override load() and run().\n"
    "• Multiple Inheritance: models subclass BaseModel + HFModelMixin.\n"
    "• Multiple Decorators: @log_call and @timeit wrap run() for logging and timing."
)

class MainWindow(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master, bg="#f6f6f6")
        self.controller = controller
        self.pack(fill="both", expand=True)
        self._build()

    def _build(self):
        # Top controls
        top = tk.Frame(self, bg="#f6f6f6")
        top.pack(fill="x", padx=10, pady=10)

        tk.Label(top, text="Select Task:", font=("Segoe UI", 10)).pack(side="left")

        self.task_var = tk.StringVar()
        self.task_combo = ttk.Combobox(
            top, textvariable=self.task_var, state="readonly",
            values=self.controller.list_tasks()
        )
        self.task_combo.pack(side="left", padx=5)

        if self.controller.list_tasks():
            self.task_combo.current(0)

        self.run_btn = ttk.Button(top, text="Run", command=self.on_run_clicked)
        self.run_btn.pack(side="right")

        # Paned layout
        panes = tk.PanedWindow(self, orient="horizontal", sashwidth=4, bg="#ddd")
        panes.pack(fill="both", expand=True, padx=12, pady=8)

        # Input panel
        left = tk.Frame(panes, bg="#fff", bd=1, relief="solid")
        panes.add(left, stretch="always")
        tk.Label(left, text="Input:", font=("Segoe UI", 10, "bold")).pack(anchor="w", padx=8, pady=(8, 4))
        self.input_txt = tk.Text(left, height=12, wrap="word")
        self.input_txt.pack(fill="both", expand=True, padx=8, pady=(0, 8))

        # Output panel
        mid = tk.Frame(panes, bg="#fff", bd=1, relief="solid")
        panes.add(mid, stretch="always")
        tk.Label(mid, text="Output:", font=("Segoe UI", 10, "bold")).pack(anchor="w", padx=8, pady=(8, 4))
        self.output_txt = tk.Text(mid, height=12, wrap="word", state="disabled")
        self.output_txt.pack(fill="both", expand=True, padx=8, pady=(0, 8))

        # Info tabs
        right = tk.Frame(panes, bg="#fff", bd=1, relief="solid")
        panes.add(right, stretch="always")

        nb = ttk.Notebook(right)
        nb.pack(fill="both", expand=True)

        self.model_info = tk.Text(nb, wrap="word", state="disabled")
        nb.add(self.model_info, text="Model Info")

        self.oop_info = tk.Text(nb, wrap="word", state="disabled")
        nb.add(self.oop_info, text="OOP Explanation")

        # Status bar
        self.status_var = tk.StringVar(value="Ready")
        status = tk.Label(self, textvariable=self.status_var, anchor="w", bg="#ececec")
        status.pack(fill="x", side="bottom")

        # preload info
        self._refresh_infos()

    def _refresh_infos(self):
        task = self.task_var.get() or (self.controller.list_tasks()[0] if self.controller.list_tasks() else "")
        info = self.controller.get_model_info(task)
        self._set_text(self.model_info, self._format_kv(info))
        self._set_text(self.oop_info, OOP_EXPLANATION)

    def _format_kv(self, d: Dict[str, Any]) -> str:
        if not d:
            return "No model selected."
        return "\n".join([f"{k}: {v}" for k, v in d.items()])

    def _set_text(self, widget: tk.Text, content: str):
        widget.configure(state="normal")
        widget.delete("1.0", "end")
        widget.insert("1.0", content)
        widget.configure(state="disabled")

    def on_run_clicked(self):
        task = self.task_var.get()
        text = self.input_txt.get("1.0", "end").strip()
        if not text:
            messagebox.showwarning("Input Required", "Please enter some text.")
            return

        self.status_var.set(f"Running {task}...")
        self.run_btn.configure(state="disabled")

        def done_cb(result):
            self.after(0, lambda: self._on_done(result))

        def err_cb(exc: Exception):
            self.after(0, lambda: self._on_error(exc))

        # Pass parameters for summarization
        extra = {}
        if task == "Summarization":
            extra = {"max_length": 120, "min_length": 30, "do_sample": False}

        self.controller.run_async(task, text, done_cb, err_cb, **extra)
        self._refresh_infos()

    def _on_done(self, result):
        pretty = self._pretty_result(result)
        self._set_text(self.output_txt, pretty)
        self.status_var.set("Ready")
        self.run_btn.configure(state="normal")

    def _on_error(self, exc: Exception):
        messagebox.showerror("Error", str(exc))
        self.status_var.set("Ready")
        self.run_btn.configure(state="normal")

    def _pretty_result(self, result):
        # Sentiment: [{'label': 'POSITIVE', 'score': 0.999}]
        # Summarization: [{'summary_text': '...'}]
        if isinstance(result, list) and result and isinstance(result[0], dict):
            if "summary_text" in result[0]:
                return result[0]["summary_text"]
            if "label" in result[0] and "score" in result[0]:
                r0 = result[0]
                return f"{r0['label']} (score={r0['score']:.3f})"
        return str(result)
