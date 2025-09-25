from typing import Any, List
from transformers import pipeline
from app.models.base import BaseModel, HFModelMixin
from app.utils.decorators import log_call, timeit

class SummarizerModel(HFModelMixin, BaseModel):
    """
    Summarization model using Hugging Face pipeline.
    Shows overriding + multiple decorators.
    """
    def load(self) -> None:
        self._model = pipeline("summarization", model=self._model_id)

    @log_call
    @timeit
    def run(self, input_data: Any, **kwargs) -> List[dict]:
        self.ensure_loaded()
        text = str(input_data).strip()
        if not text:
            return [{"summary_text": ""}]
        return self._model(
            text,
            max_length=120,
            min_length=30,
            do_sample=False
        )
