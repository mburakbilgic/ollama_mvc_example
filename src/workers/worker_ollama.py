import src
from src.core.base_worker import BaseWorker



class OllamaWorker(BaseWorker):
    def __init__(self):
        super().__init__()
        self.client = src.ollama
    
    def func_list_models(self):
        """
        in CLI: ollama list
        """
        try:
            models = self.client.list_models()
            return {
                "ok": True,
                "data": models
            }
        except Exception as e:
            return {
                "ok": False,
                "error": str(e)
            }
            
    def func_pull_models(self, model_name:str):
        """
        in CLI: ollama pull <model>
        """
        try:
            models = self.client.list_models()
            
            if model_name in models:
                return {
                    "ok": True,
                    "data": "Model already exists."
                }
                
            result = self.client.pull(model_name)            
            return {
                "ok": True,
                "data": result
            }
            
        except Exception as e:
            return {
                "ok": False,
                "error": str(e) # hata kodları 400, 500, 503, 404, 401
            }

    # TODO: delete, push
