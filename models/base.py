from abc import ABC, abstractmethod
from typing import Any, Dict

class BaseModel(ABC):
    """
    Abstract base class for AI models.
    Encapsulation: keep model internals private (_model).
    """
    def __init__(self, model_id: str, task: str, brief: str):
        self._model_id = model_id
        self._task = task
        self._brief = brief
        self._model = None   # private, to be loaded later

    @abstractmethod
    def load(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def run(self, input_data: Any, **kwargs) -> Any:
        raise NotImplementedError

    @property
    def model_id(self):
        return self._model_id

    @property
    def task(self):
        return self._task

    @property
    def brief(self):
        return self._brief

    def info(self) -> Dict[str, str]:
        return {
            "Model ID": self._model_id,
            "Task": self._task,
            "About": self._brief
        }

class HFModelMixin:
    """
    Mixin for Hugging Face models.
    Will be combined with BaseModel later (multiple inheritance).
    """
    def ensure_loaded(self):
        if self._model is None:
            self.load()
