from tkinter import Tk
from app.ui.main_window import MainWindow
from app.controllers.app_controller import AppController
from app.models.sentiment import SentimentModel   # Member 2 adds this

def create_models_registry():
    # Member 2 integrates Sentiment Analysis model from Hugging Face
    return {
        "Sentiment Analysis": SentimentModel(
            model_id="distilbert-base-uncased-finetuned-sst-2-english",
            task="sentiment-analysis",
            brief="Binary sentiment classifier fine-tuned on SST-2 dataset."
        )
    }

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
