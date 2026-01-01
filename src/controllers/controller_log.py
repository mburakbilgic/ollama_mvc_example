from fastapi import APIRouter
import src
from src.views.view_log import (
    log_list_view, 
    log_level_set_view,
    error_view
)
from src.core.worker_registry import WorkerRegistry

router = APIRouter(prefix="/log", tags=["logs"])
worker = WorkerRegistry.log

@router.get("/")
async def get_logs(level:str | None = None):
    try:
        logs = worker.func_get_logs(level)
        return log_list_view(level, logs)
    except Exception as e:
        src.logger.error(str(e))
        return error_view(str(e))

@router.post("/level/{level}")
async def set_log_level(level:str):
    try:
        result = worker.func_set_log_level(level)
        src.logger.debug(result)
        return log_level_set_view(result)
    except Exception as e:
        src.logger.error(str(e))
        return error_view(str(e))