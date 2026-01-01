from src.core.model_registry import ModelRegistry as MR

def resp_model_list(models):
    return MR.ResponseOllamaModelList(
        count=len(models),
        models=models
    )
    
def resp_model_result(model, result):
    return MR.ResponseOllamaPull(
        model=model,
        result=result
    )
      
def resp_error(message):
    return MR.ResponseOllamaError(
        message=message
    )