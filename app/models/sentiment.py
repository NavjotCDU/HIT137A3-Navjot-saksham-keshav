from typing import Any, List
from transformers import pipeline
from app.models.base import BaseModel, HFModelMixin
from app.utils.decorators import log_call, timeit

class SentimentModel(HFModelMixin, BaseModel):
    """
    Sentiment Analysis model using Hugging Face pipeline.
    Demonstrates:
    - Multiple inheritance (HFModelMixin + BaseModel)
    - Method overriding (load, run)
    - Multiple decorators (@log_call, @timeit)
    """
    def load(self) -> None:
        self._model = pipeline("sentiment-analysis", model=self._model_id)

    @log_call
    @timeit
    def run(self, input_data: Any, **kwargs) -> List[dict]:
        self.ensure_loaded()
        text = str(input_data).strip()
        if not text:
            return [{"label": "NEUTRAL", "score": 0.0}]
        return self._model(text)