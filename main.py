from tkinter import Tk
from app.ui.main_window import MainWindow
from app.controllers.app_controller import AppController
from app.models.sentiment import SentimentModel
from app.models.summarizer import SummarizerModel   # NEW

def create_models_registry():
    return {
        "Sentiment Analysis": SentimentModel(
            model_id="distilbert-base-uncased-finetuned-sst-2-english",
            task="sentiment-analysis",
            brief="Binary sentiment classifier fine-tuned on SST-2 dataset."
        ),
        "Summarization": SummarizerModel(
            model_id="sshleifer/distilbart-cnn-12-6",
            task="summarization",
            brief="Distilled BART model fine-tuned on CNN/DailyMail for text summarization."
        )
    }

def main():
    root = Tk()
    root.title("HIT137 AI Studio")
    root.geometry("1000x650")
    models = create_models_registry()
    controller = AppController(models_registry=models)
    app = MainWindow(root, controller)
    root.mainloop()

if __name__ == "__main__":
    main()
