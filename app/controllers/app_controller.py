from typing import Dict, Any

class AppController:
    """Central controller connecting UI with models (empty for now)."""
    def __init__(self, models_registry: Dict[str, Any]):
        self._models = models_registry

    def list_tasks(self):
        return list(self._models.keys())

    def get_model_info(self, task_key: str):
        return self._models[task_key].info() if task_key in self._models else {}
