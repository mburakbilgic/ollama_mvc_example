from src.core.model_registry import ModelRegistry as MR



def log_list_view(level, logs):
    return MR.ResponseLogList(
        level=level or "ALL",
        count=len(logs),
        logs=logs
    )
    
def log_level_set_view(result):
    return MR.ResponseLogLevelSet(
        level=result["level"],
        message=result["message"]
    )
    
def error_view(error:str):
    return MR.ResponseLogError(
        error=error
    )