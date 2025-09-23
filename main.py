from tkinter import Tk
from app.ui.main_window import MainWindow
from app.controllers.app_controller import AppController

def create_models_registry():
    # Empty for now – Member 2 and 3 will add real models
    return {}

def main():
    root = Tk()
    root.title("HIT137 AI Studio")
    root.geometry("800x500")
    models = create_models_registry()
    controller = AppController(models_registry=models)
    app = MainWindow(root, controller)
    root.mainloop()

if __name__ == "__main__":
    main()
